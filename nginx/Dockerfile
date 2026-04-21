FROM nginx:alpine

# Копируем конфиг Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Healthcheck
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD wget --quiet --tries=1 --spider http://localhost/health || exit 1

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
