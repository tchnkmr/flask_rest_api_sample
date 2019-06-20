from flask import Blueprint, request, abort, jsonify

from models import db, User

# api Blueprint作成　http://host/api 以下のものはここのルールで処理される
api = Blueprint('api', __name__, url_prefix='/api')


# エンドポイント http:/host/api/users, GETメソッドのみ受け付ける
# routeは複数指定も可能、methodsはリストなので複数指定可能
@api.route('/users', methods=['GET'])
def list_user():
    # クエリーパラメータ取得 request.args.get
    # 第一引数:パラメータ名、default=で初期値、type=で変換する型を指定できる
    q_limit = request.args.get('limit', default=-1, type=int)
    q_offset = request.args.get('offset', default=0, type=int)

    if q_limit == -1:
        # DBから全件取得
        users = User.query.all()
    else:
        # DBからoffset, limitを使用して取得
        users = User.query.offset(q_offset).limit(q_limit)

    # jsonレスポンス返却
    # jsonifyにdict型オブジェクトを設定するとjsonデータのレスポンスが生成される
    return jsonify({'users': [user.to_dict() for user in users]})


# URL中のパラメータ取得 <type:variable_name>
# type: string(default), int, float, path, uuid
# variable_name: 変数名
@api.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id=None):
    # DBからフィルタリングして取得
    user = User.query.filter_by(id=user_id).first()
    return jsonify(user.to_dict())


@api.route('/users', methods=['POST'])
def post_user():
    # jsonリクエストから値取得
    payload = request.json
    name = payload.get('name')
    age = payload.get('age')

    # レコードの登録 新規作成したオブジェクトをaddしてcommit
    user = User(name, age)
    db.session.add(user)
    db.session.commit()

    response = jsonify(user.to_dict())
    # レスポンスヘッダ設定
    response.headers['Location'] = '/api/users/%d' % user.id
    # HTTPステータスを200以外で返却したい場合
    return response, 201


@api.route('/users/<user_id>', methods=['PUT'])
def put_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        # エラーハンドラーに処理を移す場合
        # ステータスコード、dict型にてメッセージ等を設定できる
        abort(404, {'code': 'Not found', 'message': 'user not found'})

    # レコードの更新 オブジェクトの値を更新してcommit
    payload = request.json
    user.name = payload.get('name')
    user.age = payload.get('age')
    db.session.commit()

    return jsonify(user.to_dict())


@api.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        abort(404, {'code': 'Not found', 'message': 'user not found'})

    # レコードの削除 deleteしてcommit
    db.session.delete(user)
    db.session.commit()

    return jsonify(None), 204


# エラーのハンドリング errorhandler(xxx)を指定、複数指定可能
# ここでは400,404をハンドリングする
@api.errorhandler(400)
@api.errorhandler(404)
def error_handler(error):
    # error.code: HTTPステータスコード
    # error.description: abortで設定したdict型
    return jsonify({'error': {
        'code': error.description['code'],
        'message': error.description['message']
    }}), error.code
