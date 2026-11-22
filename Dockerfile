FROM nginx:alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html commercial-window-cleaning.html graffiti-removal.html gutter-cleaning.html contact.html privacy.html /usr/share/nginx/html/
COPY css /usr/share/nginx/html/css
COPY js /usr/share/nginx/html/js
COPY images /usr/share/nginx/html/images
COPY media /usr/share/nginx/html/media
