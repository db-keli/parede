from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Security
import jwt
from passlib.context import CryptContext
import datetime

class AuthHandler:
    security = HTTPBearer
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret_key = "super-secret-key"
    
    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)
    
    def encode_token(self, user_id):
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=30),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        
        return jwt.encode(payload, self.secret_key, algorithm='HS256')
    
    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise Exception('Signature expired. Please log in again.')
        except jwt.InvalidTokenError:
            raise Exception('Invalid token. Please log in again.')
        
    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)