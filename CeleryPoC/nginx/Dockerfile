FROM nginx

# Remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir -p /data/nginx/cache

# Replace with our own nginx.conf
COPY nginx.conf /etc/nginx/conf.d/