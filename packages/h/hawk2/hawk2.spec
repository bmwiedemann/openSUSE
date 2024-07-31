#
# spec file for package hawk2
#
# Copyright (c) 2023 SUSE LLC
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

%define rb_ruby_suffix 		ruby3.3
%define rb_build_versions       %rb_default_ruby
%define rb_build_ruby_abis      %rb_default_ruby_abi

Name:           hawk2
Summary:        HA Web Konsole
License:        GPL-2.0-only
Group:          %{pkg_group}
Version:        2.6.5+git.1722332489.55c71c1
Release:        0
URL:            http://www.clusterlabs.org/wiki/Hawk
Source:         %{name}-%{version}.tar.bz2
Source1:        sysconfig.hawk
Source2:        js-routes-1.4.1.gem
Source100:      hawk-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       ha-cluster-webui
Obsoletes:      hawk <= 1.1.0
Provides:       hawk = %{version}
Requires:       crmsh >= 3.0.0
Requires:       graphviz
Requires:       graphviz-gd
Requires:       hawk-apiserver
Requires(post): %fillup_prereq
# Need a font of some kind for graphviz to work correctly (bsc#931950)
Requires:       dejavu
Requires:       pacemaker >= 1.1.8
Recommends:     graphviz-gnome
Requires:       iproute2
PreReq:         permissions
BuildRequires:  fdupes
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
# declare the user/group we create in the preinstall script
Provides:       user(%{uname})
Provides:       greoup(%{gname})

BuildRequires:  distribution-release
BuildRequires:  timezone
BuildRequires:  rubygem(%{rb_default_ruby_abi}:bundler)
Requires:       rubygem(%{rb_default_ruby_abi}:bundler)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rails:7)
Requires:       rubygem(%{rb_default_ruby_abi}:rails:7)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:websocket-driver:0.7.6)
Requires:       rubygem(%{rb_default_ruby_abi}:websocket-driver:0.7.6)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:puma) >= 5
Requires:       rubygem(%{rb_default_ruby_abi}:puma) >= 5
BuildRequires:  rubygem(%{rb_default_ruby_abi}:sass-rails:5)
Requires:       rubygem(%{rb_default_ruby_abi}:sass-rails:5)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:virtus) >= 1.0.1
Requires:       rubygem(%{rb_default_ruby_abi}:virtus) >= 1.0.1
BuildRequires:  rubygem(%{rb_default_ruby_abi}:fast_gettext) >= 1.4
Requires:       rubygem(%{rb_default_ruby_abi}:fast_gettext) >= 1.4
BuildRequires:  rubygem(%{rb_default_ruby_abi}:gettext_i18n_rails) >= 1.8
Requires:       rubygem(%{rb_default_ruby_abi}:gettext_i18n_rails) >= 1.8
BuildRequires:  rubygem(%{rb_default_ruby_abi}:gettext_i18n_rails_js) >= 1.3
Requires:       rubygem(%{rb_default_ruby_abi}:gettext_i18n_rails_js) >= 1.3
BuildRequires:  rubygem(%{rb_default_ruby_abi}:sprockets:3.7)
Requires:       rubygem(%{rb_default_ruby_abi}:sprockets:3.7)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:kramdown) >= 1.14
Requires:       rubygem(%{rb_default_ruby_abi}:kramdown) >= 1.14

# TODO: remove uglifier completely
BuildRequires:  rubygem(%{rb_default_ruby_abi}:uglifier) >= 1.14
Requires:       rubygem(%{rb_default_ruby_abi}:uglifier) >= 1.14

BuildRequires:  rubygem(%{rb_default_ruby_abi}:execjs) >= 2.8
BuildRequires:  rubygem(%{rb_default_ruby_abi}:gettext) >= 3.2
BuildRequires:  rubygem(%{rb_default_ruby_abi}:uglifier) >= 3
# TODO: remove execjs below
Requires:       rubygem(%{rb_default_ruby_abi}:execjs) >= 2.8

# Help OBS scheduler:
BuildRequires:  rubygem(%{rb_default_ruby_abi}:mail) >= 2.8
BuildRequires:  rubygem(%{rb_default_ruby_abi}:tilt) >= 2
#/Help OBS scheduler

BuildRequires:  git
BuildRequires:  nodejs >= 10
BuildRequires:  pam-devel
BuildRequires:  shadow

%description
A web-based GUI for managing and monitoring the Pacemaker
High-Availability cluster resource manager.

%prep
%setup

%build

mkdir -p hawk/vendor/cache
install -D -m0644 %{S:2} hawk/vendor/cache
export GEM_HOME=$PWD/hawk/vendor
gem install hawk/vendor/cache/*.gem

sed -i 's$#!/.*$#!%{_bindir}/ruby.%{rb_ruby_suffix}$' hawk/bin/rails
sed -i 's$#!/.*$#!%{_bindir}/ruby.%{rb_ruby_suffix}$' hawk/bin/rake
sed -i 's$#!/.*$#!%{_bindir}/ruby.%{rb_ruby_suffix}$' hawk/bin/bundle
pushd hawk
if [ -x /usr/bin/bundle.ruby.%{rb_ruby_suffix} ]; then
	bundlerexe=bundle.ruby.%{rb_ruby_suffix}
else
	bundlerexe=bundle.%{rb_ruby_suffix}
fi
$bundlerexe exec bin/rails version
popd
export NOKOGIRI_USE_SYSTEM_LIBRARIES=1
CFLAGS="${CFLAGS} ${RPM_OPT_FLAGS}"
export CFLAGS
make WWW_BASE=%{www_base} WWW_TMP=%{www_tmp} WWW_LOG=%{www_log} INIT_STYLE=%{init_style} LIBDIR=%{_libdir} BINDIR=%{_bindir} SBINDIR=%{_sbindir} RUBY_SUFFIX=.%{rb_ruby_suffix}
# We need the Gemfile.lock only to set the permissions
# (see %attr(-, %{uname},%{gname})%{www_base}/hawk/Gemfile.lock)
# The content shoulhawk/Gemfile.lockd be generated locally.
# Btw, I tried "> hawk/Gemfile.lock" instead of "rm + touch"
# but there was a checksum error. So let's do "rm + touch".
rm hawk/Gemfile.lock
touch hawk/Gemfile.lock

%install
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
%fdupes %{buildroot}
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

# A workaround. Hawk fails with the newer js-routes-2.x.y
# And we don't want to submit the js-routes-1.4.1 to the factory
# So let's attach js-routes-1.4.1 and
# update it to the version 2 later (TODO!)
gem install --local %{www_base}/hawk/vendor/cache/js-routes-1.4.1.gem

%preun
%service_del_preun hawk.service hawk-backend.service

%postun
%service_del_postun hawk.service hawk-backend.service

%files -f hawk.lang
%defattr(644,root,root,755)
%{_fillupdir}/sysconfig.hawk
%attr(4750, root, %{gname})%{_sbindir}/hawk_chkpwd
%dir %{www_base}/hawk
# To let the hacluster write the hawk/Gemfile.lock
%attr(-, %{uname},%{gname})%{www_base}/hawk/Gemfile.lock
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
%{www_base}/hawk/Gemfile.lock
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

%{_unitdir}/hawk.service
%{_unitdir}/hawk-backend.service
%attr(-,root,root) %{_sbindir}/rchawk

%changelog
