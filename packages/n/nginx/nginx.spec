#
# spec file for package nginx
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{!?vim_data_dir:%global vim_data_dir %{_datadir}/vim/%(readlink %{_datadir}/vim/current)}
%define pkg_name       nginx
%define nginx_upstream_check_version 0.3.0
%define nginx_upstream_check_module_path nginx_upstream_check_module-%{nginx_upstream_check_version}
%define src_install_dir %{_prefix}/src/%{name}
%if 0%{?is_opensuse}
%bcond_without extra_modules
%else
%bcond_with    extra_modules
%endif
#
# keep in sync with ngx_conditionals in nginx-macros
%if 0%{?suse_version} != 1315 || 0%{?is_opensuse}
%bcond_without ngx_libatomic
%else
%bcond_with    ngx_libatomic
%endif
%if 0%{?suse_version} > 1220
%bcond_without ngx_http2
%bcond_without ngx_pcre_jit
%bcond_without systemd
%else
%bcond_with    ngx_http2
%bcond_with    ngx_pcre_jit
%bcond_with    systemd
%endif
%bcond_with    ngx_cpp_test
%bcond_with    ngx_google_perftools
#
%if %{with systemd}
%define ngx_pid_path   /run/nginx.pid
%define ngx_lock_path  /run/nginx.lock
%else
%define ngx_pid_path   %{_localstatedir}/run/nginx.pid
%define ngx_lock_path  %{_localstatedir}/run/nginx.lock
%endif
#
Name:           nginx
Version:        1.19.6
Release:        0
Summary:        A HTTP server and IMAP/POP3 proxy server
License:        BSD-2-Clause
Group:          Productivity/Networking/Web/Proxy
URL:            https://nginx.org
Source0:        https://nginx.org/download/%{name}-%{version}.tar.gz
Source1:        nginx.init
Source2:        nginx.logrotate
Source3:        nginx.service
Source4:        https://github.com/yaoweibin/nginx_upstream_check_module/archive/v%{nginx_upstream_check_version}/%{nginx_upstream_check_module_path}.tar.gz
Source9:        nginx.sysusers
Source100:      nginx.rpmlintrc
Source101:      https://nginx.org/download/%{name}-%{version}.tar.gz.asc
Source102:      https://nginx.org/keys/mdounin.key#/%{name}.keyring
# PATCH-FIX-UPSTREAM nginx-1.11.2-no_Werror.patch
Patch0:         nginx-1.11.2-no_Werror.patch
# PATCH-FIX-OPENSUSE nginx-1.11.2-html.patch
Patch1:         nginx-1.11.2-html.patch
# PATCH-FIX-UPSTREAM nginx-1.2.4-perl_vendor_install.patch
Patch2:         nginx-1.2.4-perl_vendor_install.patch
# PATCH-FIX-UPSTREAM fix /etc/nginx/nginx.conf to suit Linux env
Patch3:         nginx-1.6.1-default_config.patch
# PATCH-FIX-UPSTREAM nginx-aio.patch fix support for Linux AIO
Patch4:         nginx-aio.patch
# PATCH-FIX-UPSTREAM check_1.9.2+.patch
Patch5:         check_1.9.2+.patch
# keep Buildrequires for the libraries and everything in sync with the requires in the nginx-source package
BuildRequires:  gcc-c++
BuildRequires:  gd-devel
BuildRequires:  libxslt-devel
BuildRequires:  nginx-macros
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig
BuildRequires:  vim
BuildRequires:  zlib-devel
%requires_eq    perl
#
Recommends:     logrotate
Recommends:     nginx-module-fancyindex
Recommends:     nginx-module-geoip2
Recommends:     nginx-module-headers-more
Recommends:     nginx-module-http-flv
Recommends:     vim-plugin-nginx
Provides:       http_daemon
Provides:       httpd
#
%if %{with ngx_google_perftools}
BuildRequires:  google-perftools-devel
%endif
#
%if %{with ngx_libatomic}
BuildRequires:  libatomic-ops-devel
%endif
#
%if %{with systemd}
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(systemd)
%{?systemd_ordering}
%sysusers_requires
%else
Requires(pre):  %fillup_prereq
Requires(pre):  %insserv_prereq
Requires(pre):  shadow
%endif

%description
nginx [engine x] is a HTTP server and IMAP/POP3 proxy server written by Igor Sysoev.
It has been running on many heavily loaded Russian sites for more than two years.

%package -n vim-plugin-nginx
Summary:        VIM support for nginx config files
Group:          Productivity/Text/Editors
%requires_eq    vim
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description -n vim-plugin-nginx
nginx [engine x] is a HTTP server and IMAP/POP3 proxy server written by Igor Sysoev.
It has been running on many heavily loaded Russian sites for more than two years.

This package holds the VIM support for nginx config files.

%package -n nginx-source
Summary:        The nginx source
Group:          Development/Sources
Requires:       gcc-c++
Requires:       gd-devel
Requires:       libxslt-devel
Requires:       nginx = %{version}
Requires:       openssl-devel
Requires:       pcre-devel
Requires:       pkgconfig
Requires:       vim
Requires:       zlib-devel
%requires_ge    nginx-macros
BuildArch:      noarch
%if %{with  ngx_libatomic}
Requires:       libatomic-ops-devel
%endif

%description -n nginx-source
The source of nginx [engine x] HTTP server and IMAP/POP3 proxy server.

%prep
%setup -q -n %{pkg_name}-%{version} -a 4
%patch0 -p1
%patch1 -p1
%patch2
%patch3
%patch4 -p1
%if %{with ngx_extra_modules}
%patch5
%endif

perl -pi -e 's|\r\n|\n|g' contrib/geo2nginx.pl
# we just use lib here because nginx loads them relative to _prefix
perl -pi -e 's|#LIBDIR#|%{_lib}|g' conf/nginx.conf

%if %{with systemd}
sed -i "s/\/var\/run/\/run/" conf/nginx.conf
%endif

sed -i 's/^\(#define NGX_LISTEN_BACKLOG \).*/\1-1/' src/os/unix/ngx_linux_config.h

%build
# FIXME: you should use the %%configure macro
%{ngx_configure} \
  %if %{with ngx_extra_modules}
  --add-module=%{nginx_upstream_check_module_path} \
  %endif

%make_build
%if %{with systemd}
%sysusers_generate_pre %{SOURCE9} nginx
%endif

%install
%make_install
%perl_process_packlist

install -dpm0750 %{buildroot}%{ngx_home}/{,tmp,proxy,fastcgi,scgi,uwsgi}

install -Dpm0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/%{pkg_name}

%if %{with systemd}
install -Dpm0644 %{SOURCE3} %{buildroot}%{_unitdir}/nginx.service
ln -s -f %{_sbindir}/service %{buildroot}%{_sbindir}/rcnginx
install -Dpm0644 %{SOURCE9} %{buildroot}%{_sysusersdir}/nginx.conf
%else
install -Dpm0755 %{SOURCE1} %{buildroot}%{_sysconfdir}/init.d/%{pkg_name}
ln -s -f %{_sysconfdir}/init.d/%{pkg_name} %{buildroot}%{_sbindir}/rc%{pkg_name}
%endif

rm %{buildroot}/srv/www/htdocs/index.html

mkdir -p %{buildroot}%{ngx_doc_dir}
cp -av CHANGES* LICENSE \
  %{buildroot}%{ngx_doc_dir}

mkdir -p %{buildroot}%{vim_data_dir}/
cp -av contrib/vim/* \
  %{buildroot}%{vim_data_dir}/

mkdir -p %{buildroot}%{_datadir}/nginx/
mkdir -p %{buildroot}%{ngx_conf_dir}/vhosts.d/
mkdir -p %{buildroot}%{ngx_conf_dir}/conf.d/

chmod a+rx contrib/geo2nginx.pl
cp -av contrib/geo2nginx.pl contrib/unicode2nginx/ \
  %{buildroot}%{_datadir}/nginx/

mkdir -p %{buildroot}%{src_install_dir}
tar -xzf %{SOURCE0} --strip-components=1 -C %{buildroot}%{src_install_dir}

copydocs() {
  subdir=$1;
  shift;
  mkdir -p %{buildroot}%{ngx_doc_dir}/$subdir/
  pushd $subdir
  cp -av $* %{buildroot}%{ngx_doc_dir}/$subdir/
  popd
}

copydocs %{nginx_upstream_check_module_path} \
  doc/*

%post
%if %{with systemd}
%service_add_post nginx.service
%else
%fillup_and_insserv %{pkg_name}
%endif

%preun
%if %{with systemd}
%service_del_preun nginx.service
%else
%stop_on_removal %{pkg_name}
%endif

%postun
%if %{with systemd}
%service_del_postun nginx.service
%else
%restart_on_update %{pkg_name}
%insserv_cleanup
%endif

%if %{with systemd}
%pre -f nginx.pre
%service_add_pre nginx.service
%else
%pre
%{_sbindir}/groupadd -r %{ngx_user_group} &>/dev/null ||:
%{_sbindir}/useradd -g %{ngx_user_group} -s /bin/false -r -c "user for %{ngx_user_group}" -d %{ngx_home} %{ngx_user_group} &>/dev/null ||:
%endif

%files
%dir %{ngx_conf_dir}/
%dir %{ngx_conf_dir}/vhosts.d
%dir %{ngx_conf_dir}/conf.d
%config(noreplace) %{ngx_conf_dir}/koi-utf
%config(noreplace) %{ngx_conf_dir}/koi-win
%config(noreplace) %{ngx_conf_dir}/fastcgi_params
%config %{ngx_conf_dir}/fastcgi_params.default
%config(noreplace) %{ngx_conf_dir}/mime.types
%config %{ngx_conf_dir}/mime.types.default
%config(noreplace) %{ngx_conf_dir}/nginx.conf
%config %{ngx_conf_dir}/nginx.conf.default
%config(noreplace) %{ngx_conf_dir}/fastcgi.conf
%config %{ngx_conf_dir}/fastcgi.conf.default
%config(noreplace) %{ngx_conf_dir}/win-utf
%config(noreplace) %{ngx_conf_dir}/scgi_params
%config %{ngx_conf_dir}/scgi_params.default
%config(noreplace) %{ngx_conf_dir}/uwsgi_params
%config %{ngx_conf_dir}/uwsgi_params.default
%{perl_vendorarch}/auto/nginx/
%{perl_vendorarch}/nginx.pm
%{ngx_sbin_path}
%dir %{_libdir}/nginx/
%dir %{ngx_module_dir}/
%{ngx_module_dir}/ngx_http_image_filter_module.so
%{ngx_module_dir}/ngx_http_perl_module.so
%{ngx_module_dir}/ngx_http_xslt_filter_module.so
%{ngx_module_dir}/ngx_mail_module.so
%{ngx_module_dir}/ngx_stream_module.so
%{_mandir}/man3/nginx.3pm*
/srv/www/htdocs/50x.html
%if 0%{?suse_version} && 0%{?suse_version} < 1140
%{_localstatedir}/adm/perl-modules/%{name}
%endif
%{_sbindir}/rc%{pkg_name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{pkg_name}
%dir %attr(750,%{ngx_user_group},%{ngx_user_group}) %{_localstatedir}/log/nginx/
%dir %attr(750,%{ngx_user_group},%{ngx_user_group}) %{ngx_home}/
%dir %attr(750,%{ngx_user_group},%{ngx_user_group}) %{ngx_tmp_http}
%dir %attr(750,%{ngx_user_group},%{ngx_user_group}) %{ngx_tmp_proxy}
%dir %attr(750,%{ngx_user_group},%{ngx_user_group}) %{ngx_tmp_fcgi}
%dir %attr(750,%{ngx_user_group},%{ngx_user_group}) %{ngx_tmp_scgi}
%dir %attr(750,%{ngx_user_group},%{ngx_user_group}) %{ngx_tmp_uwsgi}
%doc %{ngx_doc_dir}
%if %{with systemd}
%{_unitdir}/nginx.service
%{_sysusersdir}/nginx.conf
%else
%{_sysconfdir}/init.d/%{pkg_name}
%endif
%{_datadir}/nginx/

%files -n vim-plugin-nginx
%license LICENSE
%dir %{vim_data_dir}/ftdetect/
%{vim_data_dir}/ftdetect/nginx.vim
%{vim_data_dir}/ftplugin/nginx.vim
%{vim_data_dir}/indent/nginx.vim
%{vim_data_dir}/syntax/nginx.vim

%files -n nginx-source
%{src_install_dir}

%changelog
