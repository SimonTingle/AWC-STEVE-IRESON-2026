FROM nginx:alpine
COPY index.html commercial-window-cleaning.html graffiti-removal.html gutter-cleaning.html contact.html privacy.html /usr/share/nginx/html/
COPY css /usr/share/nginx/html/css
COPY js /usr/share/nginx/html/js
COPY images /usr/share/nginx/html/images
COPY media /usr/share/nginx/html/media
RUN printf 'server{listen 80;root /usr/share/nginx/html;index index.html;gzip on;gzip_types text/css application/javascript image/svg+xml;location ~* \\.(jpg|png|webm|css|js)$ {expires 30d;add_header Cache-Control "public";}location / {try_files $uri $uri.html =404;}}' > /etc/nginx/conf.d/default.conf
