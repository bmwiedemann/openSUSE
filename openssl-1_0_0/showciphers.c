#include <openssl/err.h>
#include <openssl/ssl.h>

int main() {
    unsigned int i;
    SSL_CTX *ctx;
    SSL *ssl;
    SSL_METHOD *meth;
    meth = SSLv23_client_method();
    SSLeay_add_ssl_algorithms();
    ctx = SSL_CTX_new(meth);
    if (ctx == NULL) return 0;
        ssl = SSL_new(ctx);
    if (!ssl)
        return 0;
    for (i=0; ; i++) {
        int j, k;
        SSL_CIPHER *sc;
        sc = (meth->get_cipher)(i);
        if (!sc)
            break;
        k = SSL_CIPHER_get_bits(sc, &j);
        printf("%s\n", sc->name);
    }
    return 0;
}
