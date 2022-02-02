#include <openssl/err.h>
#include <openssl/ssl.h>

int main() {
    SSL_CTX *ctx = NULL;
    SSL *ssl = NULL;
    STACK_OF(SSL_CIPHER) *sk = NULL;
    const SSL_METHOD *meth = TLS_server_method();
    int i;
    const char *p;

    ctx = SSL_CTX_new(meth);
    if (ctx == NULL)
        return 1;
    ssl = SSL_new(ctx);
    if (ssl == NULL)
        return 1;
    sk = SSL_get_ciphers(ssl);
    for (i = 0; i < sk_SSL_CIPHER_num(sk); i++) {
        const SSL_CIPHER *c = sk_SSL_CIPHER_value(sk, i);
        p = SSL_CIPHER_get_name(c);
        if (p == NULL)
            break;
        printf("%s\n", p);
    }
    return 0;
}
