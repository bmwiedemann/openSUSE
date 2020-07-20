php_admin_flag      display_errors                  off
php_admin_flag      log_errors                      on
#php_admin_value     error_log                       logs/errors

php_admin_flag      magic_quotes_gpc                off
php_admin_flag      magic_quotes_runtime            off
php_admin_flag      register_globals                off
php_admin_flag      suhosin.session.encrypt         off
php_admin_flag      zlib.output_compression         off

php_admin_value     upload_max_filesize             5M
php_admin_value     post_max_size                   6M
php_admin_value     memory_limit                    64M

php_admin_flag      session.auto_start              off
#php_admin_value     session.cookie_path             /
#php_admin_value     session.hash_function           sha256
php_admin_value     session.gc_maxlifetime          21600
php_admin_value     session.gc_divisor              500
php_admin_value     session.gc_probability          1
# http://bugs.php.net/bug.php?id=30766
php_admin_value     mbstring.func_overload          0
