from common import Session

from first import Domain_ as FirstDomain
from second import Domain_ as SecondDomain


if __name__ == '__main__':
    session = Session()
    print session.query(SecondDomain).one()
    print session.query(FirstDomain).one()
