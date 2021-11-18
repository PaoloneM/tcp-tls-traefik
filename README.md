# Multiple TCP services served through Traefik with SSL

## Prepare

```
mkdir .cets
cd .certs
../certs.sh *.mysite.com
cd ..
```

## Run

```
docker compose up -d
python tcp_tls_client.py tcptls1
python tcp_tls_client.py tcptls2
```