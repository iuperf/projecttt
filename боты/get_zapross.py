import flask

import goroskop

blueprint = flask.Blueprint(
    'getting',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/goroskop/<int:mounth>/<int:day>', methods=['GET'])
def get_one(mounth, day):
    return goroskop.z_s(goroskop.zodiac_sign(day, mounth))


