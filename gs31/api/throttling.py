from rest_framework.throttling import UserRateThrottle

class JackrateThrottle(UserRateThrottle):
    scope = 'jack'
