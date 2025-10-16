#
# spec file for package hawk2
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%define	vendor_ruby	vendor_ruby
%define	init_style	suse
%define	pkg_group	Productivity/Clustering/HA

%define www_base %{_datadir}
%define www_tmp  %{_localstatedir}/lib/hawk/tmp
%define www_log  %{_localstatedir}/log/hawk
%define gname haclient
%define uname hacluster

%define rb_build_versions %{rb_default_ruby}
%define rb_build_abi      %{rb_default_ruby_abi}
%define rb_suffix         %{rb_default_ruby_suffix}

%define install_gem_path /usr/libexec/hawk/vendor

Name:           hawk2
Summary:        HA Web Konsole
License:        GPL-2.0-only
Group:          %{pkg_group}
Version:        2.7.0+git.1742310530.bfcd0e2c
Release:        0
URL:            http://www.clusterlabs.org/wiki/Hawk
Source:         %{name}-%{version}.tar.bz2
Source1:        sysconfig.hawk

Source2:       rake-13.2.1.gem
Source3:       base64-0.2.0.gem
Source4:       benchmark-0.4.0.gem
Source5:       bigdecimal-3.1.9.gem
Source6:       concurrent-ruby-1.3.5.gem
Source7:       connection_pool-2.5.0.gem
Source8:       drb-2.2.1.gem
Source9:       i18n-1.14.7.gem
Source10:       logger-1.7.0.gem
Source11:       minitest-5.25.5.gem
Source12:       securerandom-0.4.1.gem
Source13:       tzinfo-2.0.6.gem
Source14:       uri-1.0.4.gem
Source15:       activesupport-8.0.2.1.gem
Source16:       builder-3.3.0.gem
Source17:       erubi-1.13.1.gem
Source18:       mini_portile2-2.8.8.gem
Source19:       racc-1.8.1.gem
Source20:       nokogiri-1.18.5.gem
Source21:       rails-dom-testing-2.2.0.gem
Source22:       crass-1.0.6.gem
Source23:       loofah-2.24.0.gem
Source24:       rails-html-sanitizer-1.6.2.gem
Source25:       actionview-8.0.2.1.gem
Source26:       rack-3.1.18.gem
Source27:       rack-session-2.1.1.gem
Source28:       rack-test-2.2.0.gem
Source29:       useragent-0.16.11.gem
Source30:       actionpack-8.0.2.1.gem
Source31:       nio4r-2.7.4.gem
Source32:       websocket-extensions-0.1.5.gem
Source33:       websocket-driver-0.7.7.gem
Source34:       zeitwerk-2.7.2.gem
Source35:       actioncable-8.0.2.1.gem
Source36:       globalid-1.2.1.gem
Source37:       activejob-8.0.2.1.gem
Source38:       activemodel-8.0.2.1.gem
Source39:       timeout-0.4.3.gem
Source40:       activerecord-8.0.2.1.gem
Source41:       marcel-1.0.4.gem
Source42:       activestorage-8.0.2.1.gem
Source43:       mini_mime-1.1.5.gem
Source44:       date-3.4.1.gem
Source45:       net-protocol-0.2.2.gem
Source46:       net-imap-0.5.8.gem
Source47:       net-pop-0.1.2.gem
Source48:       net-smtp-0.5.1.gem
Source49:       mail-2.8.1.gem
Source50:       actionmailbox-8.0.2.1.gem
Source51:       actionmailer-8.0.2.1.gem
Source52:       actiontext-8.0.2.1.gem
Source53:       thread_safe-0.3.6.gem
Source54:       descendants_tracker-0.0.4.gem
Source55:       ice_nine-0.11.2.gem
Source56:       axiom-types-0.1.1.gem
Source57:       coercible-1.0.0.gem
Source58:       execjs-2.10.0.gem
Source59:       forwardable-1.3.3.gem
Source60:       singleton-0.3.0.gem
Source61:       prime-0.1.3.gem
Source62:       fast_gettext-4.1.0.gem
Source63:       ffi-1.17.1.gem
Source64:       locale-2.1.4.gem
Source65:       text-1.3.1.gem
Source66:       gettext-3.5.1.gem
Source67:       gettext_i18n_rails-1.13.0.gem
Source68:       json-2.10.2.gem
Source69:       po_to_json-2.0.0.gem
Source70:       prettyprint-0.2.0.gem
Source71:       pp-0.6.2.gem
Source72:       stringio-3.1.6.gem
Source73:       psych-5.2.3.gem
Source74:       rdoc-6.13.1.gem
Source75:       io-console-0.8.0.gem
Source76:       reline-0.6.0.gem
Source77:       irb-1.15.1.gem
Source78:       rackup-2.2.1.gem
Source79:       thor-1.4.0.gem
Source80:       railties-8.0.2.1.gem
Source81:       rails-8.0.2.1.gem
Source82:       gettext_i18n_rails_js-2.1.0.gem
Source83:       sorbet-runtime-0.5.11966.gem
Source84:       js-routes-2.3.5.gem
Source85:       rexml-3.4.1.gem
Source86:       kramdown-2.5.1.gem
Source87:       puma-6.6.0.gem
Source88:       sassc-2.4.0.gem
Source89:       sprockets-4.2.1.gem
Source90:       sprockets-rails-3.5.2.gem
Source91:       tilt-2.6.0.gem
Source92:       sassc-rails-2.1.2.gem
Source93:       sass-rails-6.0.0.gem
Source94:       uglifier-4.2.1.gem
Source95:       virtus-2.0.0.gem

Source100:      hawk-rpmlintrc
Patch1:         make-sle16-compatible.patch
Patch2:         gemfile-lock.patch
Patch3:         update-hawk-backend-service.patch
Patch4:         fix-mtime.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       ha-cluster-webui
Obsoletes:      hawk <= 1.1.0
Provides:       hawk = %{version}
Requires:       crmsh >= 3.0.0
Requires:       graphviz
Requires:       graphviz-gd
Requires:       hawk-apiserver
Requires:       openssl
Requires(post): %fillup_prereq
# Need a font of some kind for graphviz to work correctly (bsc#931950)
Requires:       dejavu
Requires:       pacemaker >= 1.1.8
Recommends:     graphviz-gnome
Requires:       iproute2
PreReq:         permissions
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
# declare the user/group we create in the preinstall script
Provides:       user(%{uname})
Provides:       group(%{gname})

BuildRequires:  distribution-release
BuildRequires:  timezone
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  ruby-devel
BuildRequires:  libyaml-devel
BuildRequires:  libxslt-devel
BuildRequires:  rubygem(%{rb_build_abi}:bundler)
Requires:       rubygem(%{rb_build_abi}:bundler)

BuildRequires:  git
BuildRequires:  nodejs >= 10
BuildRequires:  pam-devel
BuildRequires:  shadow

%description
A web-based GUI for managing and monitoring the Pacemaker
High-Availability cluster resource manager.

%prep
%setup -q
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1

mkdir -p hawk/vendor/cache
install -D %{_sourcedir}/*.gem hawk/vendor/cache
export GEM_HOME=$PWD/hawk/vendor
export NO_DEBUGINFO=1

pushd hawk
  bundle config set force_ruby_platform true
  bundle config set build.nokogiri --use-system-libraries=false
  bundle install --local

  %patch -P 4 -p2
popd

%build

mkdir -p hawk/vendor/cache
install -D %{_sourcedir}/*.gem hawk/vendor/cache
export GEM_HOME=$PWD/hawk/vendor
export NO_DEBUGINFO=1

pushd hawk
  find vendor -name a.out -delete
  find vendor -name "*.so.debug" -delete
  find . -name ".*" ! -name "." ! -name ".." -exec rm -rf {} +
  find vendor/gems -type f -size 0 -exec rm -rf {} +

  find vendor -type f -exec sed -i -E \
    -e '1s|^#! */usr/bin/env ruby(\.ruby3\.4)?$|#!/usr/bin/ruby|' \
    -e '1s|^#! */usr/bin/env ruby -wKU$|#!/usr/bin/ruby -wKU|' \
    -e '1s|^#! */usr/bin/env bash$|#!/usr/bin/bash|' {} \;

  sed -i 's$#!/.*$#!%{_bindir}/ruby.%{rb_suffix}$' bin/rails
  sed -i 's$#!/.*$#!%{_bindir}/ruby.%{rb_suffix}$' bin/rake
  sed -i 's$#!/.*$#!%{_bindir}/ruby.%{rb_suffix}$' bin/bundle

  if [ -x /usr/bin/bundle.ruby.%{rb_suffix} ]; then
      bundlerexe=bundle.ruby.%{rb_suffix}
  else
      bundlerexe=bundle.%{rb_suffix}
  fi
  $bundlerexe exec bin/rails version
popd
export NOKOGIRI_USE_SYSTEM_LIBRARIES=1
CFLAGS="${CFLAGS} ${RPM_OPT_FLAGS}"
export CFLAGS

### FYI: the 'bundle install' installs puma, not puma.ruby34 (although 'gem install puma-6.6.0.gem' installs puma.ruby34)
make WWW_BASE=%{www_base} WWW_TMP=%{www_tmp} WWW_LOG=%{www_log} INIT_STYLE=%{init_style} LIBDIR=%{_libdir} BINDIR=%{_bindir} SBINDIR=%{_sbindir} RUBY_SUFFIX=

# Clean unnecessary cache to make the build deterministic (bsc#1230275)
rm -rf ./hawk/tmp/cache/assets/sprockets
find ./hawk -name "*_make.out" -delete
find ./hawk -name "*.log" -delete
find ./hawk/locale \( -name "*.po" -o -name "*.pot" \) -exec sed -i 's/^"POT-Creation-Date:.*"/"POT-Creation-Date: 2025-09-01 00:00+0000\\n"/' {} +
find ./hawk/locale \( -name "*.po" -o -name "*.pot" \) -exec sed -i 's/^"PO-Revision-Date:.*"/"PO-Revision-Date: 2025-09-01 00:00+0000\\n"/' {} +
find ./hawk/public -name "manifest.json" -exec sed -i 's/"mtime":"[^"]*"/"mtime":"2025-09-01T00:00:00+00:00"/g' {} +
rm ./hawk/tmp/session_secret # if there is no session_secret, it's automatically generated when starting puma

%install

install -p -d -m 755 %{buildroot}%{install_gem_path}
cp -r hawk/vendor/{bin,build_info,cache,doc,extensions,gems,plugins,specifications} %{buildroot}%{install_gem_path}/
# Need to remove them before 'make install'
rm -rf hawk/vendor/{bin,build_info,cache,doc,extensions,gems,plugins,specifications}

make WWW_BASE=%{www_base} WWW_TMP=%{www_tmp} WWW_LOG=%{www_log} INIT_STYLE=%{init_style} DESTDIR=%{buildroot} install

# copy of GPL
cp COPYING %{buildroot}%{www_base}/hawk/

# Hack so missing links to docs don't kill the build
mkdir -p %{buildroot}/usr/share/doc/manual/sle-ha-geo-quick_en-pdf
mkdir -p %{buildroot}/usr/share/doc/manual/sle-ha-guide_en-pdf
mkdir -p %{buildroot}/usr/share/doc/manual/sle-ha-manuals_en
mkdir -p %{buildroot}/usr/share/doc/manual/sle-ha-geo-manuals_en
mkdir -p %{buildroot}/usr/share/doc/manual/sle-ha-nfs-quick_en-pdf
mkdir -p %{buildroot}/usr/share/doc/manual/sle-ha-install-quick_en-pdf

# mark .mo files as such (works on SUSE but not FC12, as the latter wants directory to
# be "share/locale", not just "locale", and it also doesn't support appending to %%{name}.lang)
%find_lang hawk hawk.lang
# don't ship .po files (find_lang only grabs the mos, and we don't need the pos anyway)
rm %{buildroot}%{www_base}/hawk/locale/*/hawk.po
rm %{buildroot}%{www_base}/hawk/locale/*/hawk.po.time_stamp
rm %{buildroot}%{www_base}/hawk/locale/*/hawk.edit.po
# hard link duplicate files
%fdupes %{buildroot}%{www_base}/hawk
%fdupes %{buildroot}%{install_gem_path}
# more cruft to clean up (WTF?)
rm -f %{buildroot}%{www_log}/*
# likewise .git special files
find %{buildroot}%{www_base}/hawk -type f -name '.git*' -print0 | xargs --no-run-if-empty -0 rm
%{__ln_s} -f %{_sbindir}/service %{buildroot}%{_sbindir}/rchawk

install -p -d -m 755 %{buildroot}%{_sysconfdir}/hawk
install -D -m 0644 %{S:1}  %{buildroot}%{_fillupdir}/sysconfig.hawk

%clean
rm -rf %{buildroot}

%verifyscript
%verify_permissions -e %{_sbindir}/hawk_chkpwd

%pre
getent group %{gname} >/dev/null || groupadd -r %{gname} -g 189
getent passwd %{uname} >/dev/null || useradd -r -g %{gname} -u 189 -s /sbin/nologin -c "cluster user" %{uname}
%service_add_pre hawk.service hawk-backend.service

%post
%set_permissions %{_sbindir}/hawk_chkpwd
%service_add_post hawk.service hawk-backend.service
%{fillup_only -n hawk}

%preun
%service_del_preun hawk.service hawk-backend.service

%postun
%service_del_postun hawk.service hawk-backend.service


%files -f hawk.lang
%defattr(644,root,root,755)
%{_fillupdir}/sysconfig.hawk
%attr(4750, root, %{gname})%{_sbindir}/hawk_chkpwd
%dir %{www_base}/hawk
%{www_base}/hawk/log
%{www_base}/hawk/tmp
%{www_base}/hawk/app
%{www_base}/hawk/config
%dir %{_localstatedir}/lib/hawk
%dir %{www_base}/hawk/bin
%attr(0755, root, root)%{www_base}/hawk/bin/rake
%attr(0755, root, root)%{www_base}/hawk/bin/rails
%exclude %{www_base}/hawk/bin/hawk
%attr(0755, root, root)%{www_base}/hawk/bin/generate-ssl-cert
%attr(0755, root, root)%{www_base}/hawk/bin/bundle
%attr(0750, %{uname},%{gname})%{_sysconfdir}/hawk
%dir %attr(0750, %{uname},%{gname})%{www_log}
%dir %attr(0750, %{uname},%{gname})%{www_tmp}
%attr(-, %{uname},%{gname})%{www_tmp}/cache
%attr(-, %{uname},%{gname})%{www_tmp}/explorer
%attr(-, %{uname},%{gname})%{www_tmp}/home
%attr(-, %{uname},%{gname})%{www_tmp}/pids
%attr(-, %{uname},%{gname})%{www_tmp}/sessions
%attr(-, %{uname},%{gname})%{www_tmp}/sockets
%{www_base}/hawk/locale/hawk.pot
%{www_base}/hawk/public
%{www_base}/hawk/Rakefile
# We want Gemfile to explicitelly tell puma which gems to use
%{www_base}/hawk/Gemfile
# To let the hacluster write the hawk/Gemfile.lock
%attr(-, %{uname},%{gname})%{www_base}/hawk/Gemfile.lock
%{www_base}/hawk/COPYING
%{www_base}/hawk/config.ru
%{www_base}/hawk/test
%{www_base}/hawk/spec
# itemizing content in %%{www_base}/hawk/locale to avoid
# duplicate files that would otherwise be the result of including hawk.lang
%dir %{www_base}/hawk/locale
%dir %{www_base}/hawk/locale/*
%dir %{www_base}/hawk/locale/*/*

# Not doing this itemization for %%lang files in vendor, it's frightfully
# hideous, so we're going to live with a handful of file-not-in-%%lang rpmlint
# warnings for bundled gems.
%{www_base}/hawk/vendor

%attr(0755,root,root) %{install_gem_path}/bin
%exclude %{install_gem_path}/build_info
%{install_gem_path}/cache
%doc %{install_gem_path}/doc
%dir %{install_gem_path}/..
%dir %{install_gem_path}
%{install_gem_path}/extensions
%{install_gem_path}/gems
%{install_gem_path}/plugins
%{install_gem_path}/specifications

%{_unitdir}/hawk.service
%{_unitdir}/hawk-backend.service
%attr(-,root,root) %{_sbindir}/rchawk

%exclude %{install_gem_path}/gems/bigdecimal-3.1.9/ext/bigdecimal/*
%exclude %{install_gem_path}/gems/date-3.4.1/ext/date/*
%exclude %{install_gem_path}/gems/ffi-1.17.1/ext/ffi_c/*
%exclude %{install_gem_path}/gems/io-console-0.8.0/ext/io/console/console.c
%exclude %{install_gem_path}/gems/json-2.10.2/ext/json/ext/fbuffer/fbuffer.h
%exclude %{install_gem_path}/gems/json-2.10.2/ext/json/ext/generator/generator.c
%exclude %{install_gem_path}/gems/json-2.10.2/ext/json/ext/parser/parser.c
%exclude %{install_gem_path}/gems/mini_portile2-2.8.8/test/assets/pkgconf/libxml2/libxml-2.0.pc
%exclude %{install_gem_path}/gems/mini_portile2-2.8.8/test/assets/pkgconf/libxslt/libexslt.pc
%exclude %{install_gem_path}/gems/mini_portile2-2.8.8/test/assets/pkgconf/libxslt/libxslt.pc
%exclude %{install_gem_path}/gems/mini_portile2-2.8.8/test/assets/test-cmake-1.0/hello.c
%exclude %{install_gem_path}/gems/nio4r-2.7.4/ext/libev/*
%exclude %{install_gem_path}/gems/nio4r-2.7.4/ext/nio4r/*
%exclude %{install_gem_path}/gems/nokogiri-1.18.5/ext/nokogiri/*
%exclude %{install_gem_path}/gems/nokogiri-1.18.5/gumbo-parser/src/*
%exclude %{install_gem_path}/gems/psych-5.2.3/ext/psych/*
%exclude %{install_gem_path}/gems/puma-6.6.0/ext/puma_http11/*
%exclude %{install_gem_path}/gems/sassc-2.4.0/ext/libsass/contrib/plugin.cpp
%exclude %{install_gem_path}/gems/sassc-2.4.0/ext/libsass/include/*
%exclude %{install_gem_path}/gems/sassc-2.4.0/ext/libsass/src/*
%exclude %{install_gem_path}/gems/stringio-3.1.6/ext/stringio/stringio.c
%exclude %{install_gem_path}/gems/websocket-driver-0.7.7/ext/websocket-driver/websocket_mask.c

%changelog
