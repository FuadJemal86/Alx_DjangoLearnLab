# 🔒 Security Review for Django App

## ✅ HTTPS Enforcement
- `SECURE_SSL_REDIRECT = True` forces HTTPS on all requests.
- HTTP to HTTPS redirect configured at server level.

## ✅ HSTS
- `SECURE_HSTS_SECONDS = 31536000`: Enforces HTTPS at browser level.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: Applies to all subdomains.
- `SECURE_HSTS_PRELOAD = True`: Allows preloading via browsers.

## ✅ Cookies
- `SESSION_COOKIE_SECURE = True`: Prevents cookies over HTTP.
- `CSRF_COOKIE_SECURE = True`: Prevents CSRF cookie exposure over HTTP.

## ✅ Headers
- `X_FRAME_OPTIONS = 'DENY'`: Blocks clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents MIME-sniffing.
- `SECURE_BROWSER_XSS_FILTER = True`: Helps browsers block XSS.

## 🔧 Deployment Notes
- SSL/TLS should be configured in Nginx (or hosting provider).
- Django settings assume HTTPS is active at the proxy/server.

## 🚧 Areas to Improve
- Enable CSP via django-csp or middleware
- Use Django’s `SECURE_PROXY_SSL_HEADER` if behind reverse proxy
