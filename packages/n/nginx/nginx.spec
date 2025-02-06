#
# spec file for package nginx
#
# Copyright (c) 2025 SUSE LLC
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
%define src_install_dir %{_prefix}/src/%{name}
# keep in sync with #ngx_conditionals
%bcond_with    ngx_cpp_test
%bcond_with    ngx_google_perftools
#
Name:           nginx
Version:        1.27.4
Release:        0
Summary:        A HTTP server and IMAP/POP3 proxy server
License:        BSD-2-Clause
Group:          Productivity/Networking/Web/Proxy
URL:            https://github.com/nginx/nginx
Source0:        https://github.com/nginx/nginx/releases/download/release-%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/nginx/nginx/releases/download/release-%{version}/%{name}-%{version}.tar.gz.asc
Source2:        https://nginx.org/keys/pluknet.key#/%{name}.keyring
Source3:        %{name}.rpmlintrc
Source4:        %{name}.logrotate
Source5:        %{name}.service
Source6:        %{name}.sysusers
# PATCH-FIX-UPSTREAM nginx-1.11.2-no_Werror.patch
Patch0:         %{name}-1.11.2-no_Werror.patch
# PATCH-FIX-OPENSUSE nginx-1.11.2-html.patch
Patch1:         %{name}-1.11.2-html.patch
# PATCH-FIX-UPSTREAM nginx-1.2.4-perl_vendor_install.patch
Patch2:         %{name}-perl.patch
# PATCH-FIX-UPSTREAM fix /etc/nginx/nginx.conf to suit Linux env
Patch3:         %{name}-conf.patch
# PATCH-FIX-UPSTREAM nginx-aio.patch fix support for Linux AIO
Patch4:         %{name}-aio.patch
BuildRequires:  %{name}-macros
BuildRequires:  gcc-c++
BuildRequires:  gpg2
BuildRequires:  libatomic-ops-devel
BuildRequires:  pkgconfig
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  vim
BuildRequires:  pkgconfig(gdlib)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
%requires_eq    perl
Recommends:     %{name}-module-echo
Recommends:     %{name}-module-lua
Recommends:     logrotate
Provides:       http_daemon
Provides:       httpd
%{?systemd_ordering}
%sysusers_requires

%if %{with ngx_google_perftools}
BuildRequires:  google-perftools-devel
%endif

%description
%{name} [engine x] is a HTTP server and IMAP/POP3 proxy server written by Igor Sysoev.
It has been running on many heavily loaded Russian sites for more than two years.

%package source
Summary:        The nginx source
Group:          Development/Sources
Requires:       gcc-c++
Requires:       libatomic-ops-devel
Requires:       nginx = %{version}
Requires:       pkgconfig
Requires:       vim
Requires:       pkgconfig(gdlib)
Requires:       pkgconfig(libpcre2-8)
Requires:       pkgconfig(libxslt)
Requires:       pkgconfig(openssl)
Requires:       pkgconfig(zlib)
%requires_ge    %{name}-macros
BuildArch:      noarch

%description source
The source of %{name} [engine x] HTTP server and IMAP/POP3 proxy server.

%prep
%autosetup -p1
sed -i 's/\r//g' contrib/geo2nginx.pl
sed -i -e 's|#LIBDIR#|%{_libdir}|g' -e 's|/var/run|/run|' conf/nginx.conf
sed -i 's/^\(#define NGX_LISTEN_BACKLOG \).*/\1-1/' src/os/unix/ngx_linux_config.h

%build
%{ngx_configure}

%make_build
%sysusers_generate_pre %{SOURCE6} %{name} %{name}.conf

%install
%make_install
%perl_process_packlist

install -dpm0750 %{buildroot}%{ngx_home}/{,tmp,proxy,fastcgi,scgi,uwsgi}
install -Dpm0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -Dpm0644 %{SOURCE5} %{buildroot}%{_unitdir}/%{name}.service
install -Dpm0644 %{SOURCE6} %{buildroot}%{_sysusersdir}/%{name}.conf

rm %{buildroot}/srv/www/htdocs/index.html

mkdir -p %{buildroot}%{ngx_doc_dir}
cp -av CHANGES* LICENSE %{buildroot}%{ngx_doc_dir}

mkdir -p %{buildroot}%{_datadir}/%{name}/
mkdir -p %{buildroot}%{ngx_conf_dir}/vhosts.d/
mkdir -p %{buildroot}%{ngx_conf_dir}/conf.d/

chmod a+rx contrib/geo2nginx.pl
cp -av contrib/geo2nginx.pl contrib/unicode2nginx/ %{buildroot}%{_datadir}/%{name}/

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

%check
GPGTMP=`mktemp -d`
gpg --homedir $GPGTMP -q --no-default-keyring --keyring $GPGTMP/.gpg-keyring --trust-model always --import %{SOURCE2}
gpg --homedir $GPGTMP -q --no-default-keyring --keyring $GPGTMP/.gpg-keyring --trust-model always -q --verify -- %{SOURCE1} %{SOURCE0}
rm -r $GPGTMP

%pre -f %{name}.pre
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%post
%service_add_post %{name}.service

%postun
%service_del_postun %{name}.service

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
%config %{ngx_conf_dir}/%{name}.conf.default
%config(noreplace) %{ngx_conf_dir}/fastcgi.conf
%config %{ngx_conf_dir}/fastcgi.conf.default
%config(noreplace) %{ngx_conf_dir}/win-utf
%config(noreplace) %{ngx_conf_dir}/scgi_params
%config %{ngx_conf_dir}/scgi_params.default
%config(noreplace) %{ngx_conf_dir}/uwsgi_params
%config %{ngx_conf_dir}/uwsgi_params.default
%{perl_vendorarch}/auto/%{name}/
%{perl_vendorarch}/%{name}.pm
%{ngx_sbin_path}
%dir %{_libdir}/%{name}/
%dir %{ngx_module_dir}/
%{ngx_module_dir}/ngx_http_image_filter_module.so
%{ngx_module_dir}/ngx_http_perl_module.so
%{ngx_module_dir}/ngx_http_xslt_filter_module.so
%{ngx_module_dir}/ngx_mail_module.so
%{ngx_module_dir}/ngx_stream_module.so
%{_mandir}/man3/%{name}.3pm*
%dir /srv/www
%dir /srv/www/htdocs
/srv/www/htdocs/50x.html
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %attr(750,%{ngx_user_group},%{ngx_user_group}) %{_localstatedir}/log/nginx/
%dir %attr(750,%{ngx_user_group},%{ngx_user_group}) %{ngx_home}/
%dir %attr(750,%{ngx_user_group},%{ngx_user_group}) %{ngx_tmp_http}
%dir %attr(750,%{ngx_user_group},%{ngx_user_group}) %{ngx_tmp_proxy}
%dir %attr(750,%{ngx_user_group},%{ngx_user_group}) %{ngx_tmp_fcgi}
%dir %attr(750,%{ngx_user_group},%{ngx_user_group}) %{ngx_tmp_scgi}
%dir %attr(750,%{ngx_user_group},%{ngx_user_group}) %{ngx_tmp_uwsgi}
%doc %{ngx_doc_dir}
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf
%{_datadir}/%{name}/

%files source
%{src_install_dir}

%changelog
