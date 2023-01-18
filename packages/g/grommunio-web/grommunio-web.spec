#
# spec file for package grommunio-web
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


%if 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora_version}
%global __brp_mangle_shebangs_exclude_from sabredav|vobject|generate_vcards
%endif

Name:           grommunio-web
Version:        3.1.182.52d9180
Release:        0
Summary:        Web client for access to grommunio features from the web
License:        AGPL-3.0-or-later AND GPL-3.0-only AND LGPL-2.1-only AND MIT
Group:          Productivity/Networking/Email/Clients
URL:            http://www.grommunio.com/
Source:         %name-%version.tar.xz

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
%define phpdir /etc/php8
BuildRequires:  php8-gettext
%else
# i.e. SUSE15, RHEL, etc.
%define phpdir /etc/php7
%endif
%if 0%{?sle_version} && 0%{?sle_version} < 150400
BuildRequires:  php7-gettext
BuildRequires:  php7-json
%endif
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  java >= 1.9.0
BuildRequires:  java-devel >= 1.9.0
%else
BuildRequires:  java-11-openjdk-devel
BuildRequires:  php-cli
BuildRequires:  php-json
%endif
BuildRequires:  mapi-header-php
BuildRequires:  php
BuildRequires:  xz
%if 0%{?suse_version} >= 1220
BuildRequires:  libxml2-tools
%else
BuildRequires:  libxml2
%endif
BuildArch:      noarch

Requires(pre):  user(groweb)
Requires:       gromox >= 1.27
Requires:       mapi-header-php
%if 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora_version}
Requires:       php-bcmath
Requires:       php-common
Requires:       php-ctype
Requires:       php-curl
Requires:       php-mbstring
Requires:       php-sodium
Requires:       php-sqlite3
%endif
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
Requires:       php8-bcmath
Requires:       php8-ctype
Requires:       php8-curl
Requires:       php8-gd
Requires:       php8-gettext
Requires:       php8-iconv
Requires:       php8-mbstring
Requires:       php8-openssl
Requires:       php8-sodium
Requires:       php8-sqlite
Requires:       php8-sysvshm
Requires:       php8-zip
Requires:       php8-zlib
%endif
%if 0%{?sle_version} && 0%{?sle_version} < 150400
Requires:       php7-bcmath
Requires:       php7-ctype
Requires:       php7-curl
Requires:       php7-gd
Requires:       php7-gettext
Requires:       php7-iconv
Requires:       php7-json
Requires:       php7-mbstring
Requires:       php7-openssl
Requires:       php7-sodium
Requires:       php7-sqlite
Requires:       php7-sysvshm
Requires:       php7-zip
Requires:       php7-zlib
%endif

%define langdir %_datadir/%name/server/language
%define plugindir %_datadir/%name/plugins
%define nginx_dir %_sysconfdir/nginx

%description
A web client written in PHP that makes use of HTML5, JSON and ExtJS
to allow users to make full use of the grommunio
through a web browser.

%prep
%autosetup -p1
find . -type f "(" -name "*.js" -o -name "*.php" ")" \
	-exec chmod a-x "{}" "+";
# Set git revision
echo "%version-%release" >version
echo "%version-%release" | sha1sum | cut -b 1-8 >cachebuster

%build
%make_build -j1

%install
b="%buildroot"
d="$b/%_datadir"
mkdir -p "$d"
cp -a deploy "$b/%_datadir/%name"

install -vm 644 LICENSE.txt "$b/%_datadir/%name/LICENSE.txt"

# Nginx conf
mkdir -pv "$b/usr/share/grommunio-common/nginx/locations.d"
install -Dpvm 644 build/grommunio-web.conf "$b/usr/share/grommunio-common/nginx/locations.d/"
mkdir -pv "$b/usr/share/grommunio-common/nginx/upstreams.d"
install -Dpvm 644 build/grommunio-web-upstream.conf "$b/usr/share/grommunio-common/nginx/upstreams.d/grommunio-web.conf"

# PHP-FPM
mkdir -pv "$b/%phpdir/fpm/php-fpm.d/"
install -Dpvm 644 build/pool-grommunio-web.conf "$b/%phpdir/fpm/php-fpm.d/pool-grommunio-web.conf"

# web config
mkdir -pv "$b/%_sysconfdir/grommunio-web"
mv -v "$b/%_datadir/%name/config.php.dist" "$b/%_sysconfdir/grommunio-web/config.php"
ln -sfv "%_sysconfdir/grommunio-web/config.php" "$b/%_datadir/grommunio-web/config.php"
rm -v "$b/%_datadir/%name/debug.php.dist"
mkdir -pv "$b/var/lib/%name/tmp"
mkdir -pv "$b/var/lib/%name/sqlite-index"
mkdir -pv "$b/var/lib/%name/session"
mkdir -pv "$b/var/log/grommunio"

# Signatures template scripts
mkdir -pv "$b/%_datadir/doc/grommunio-web/scripts"

for dir in "$b/%_datadir/%name/plugins"/*; do
	plugindir=$(basename "$dir")
	if [ -f "$b/%_datadir/%name/plugins/$plugindir/config.php" ]; then
		mv -v "$b/%_datadir/%name/plugins/$plugindir/config.php" "$b/%_sysconfdir/grommunio-web/config-$plugindir.php"
		ln -sv "%_sysconfdir/grommunio-web/config-$plugindir.php" "$b/%_datadir/%name/plugins/$plugindir/config.php"
	else
		echo "we did not find a config.php"
	fi
done

%if 0%{?fdupes:1}
%fdupes %buildroot/%_prefix
%endif

%post
# clear translation caches
ipcrm -M 0x950412de 2>/dev/null || :

%files
%dir %_sysconfdir/grommunio-web
%dir %phpdir
%dir %phpdir/fpm
%dir %phpdir/fpm/php-fpm.d/
%attr(0640,root,root) %phpdir/fpm/php-fpm.d/pool-grommunio-web.conf
%config(noreplace) %attr(0644,root,root) %_sysconfdir/grommunio-web/config-archive.php
%config(noreplace) %attr(0644,root,root) %_sysconfdir/grommunio-web/config-chat.php
%config(noreplace) %attr(0644,root,root) %_sysconfdir/grommunio-web/config-desktopnotifications.php
%config(noreplace) %attr(0644,root,root) %_sysconfdir/grommunio-web/config-files.php
%config(noreplace) %attr(0644,root,root) %_sysconfdir/grommunio-web/config-intranet.php
%config(noreplace) %attr(0644,root,root) %_sysconfdir/grommunio-web/config-maps.php
%config(noreplace) %attr(0644,root,root) %_sysconfdir/grommunio-web/config-mdm.php
%config(noreplace) %attr(0644,root,root) %_sysconfdir/grommunio-web/config-meet.php
%config(noreplace) %attr(0644,root,root) %_sysconfdir/grommunio-web/config-passwd.php
%config(noreplace) %attr(0644,root,root) %_sysconfdir/grommunio-web/config-smime.php
%config(noreplace) %attr(0644,root,root) %_sysconfdir/grommunio-web/config.php
%dir %_datadir/grommunio-common/
%dir %_datadir/grommunio-common/nginx/
%dir %_datadir/grommunio-common/nginx/locations.d/
%_datadir/grommunio-common/nginx/locations.d/grommunio-web.conf
%dir %_datadir/grommunio-common/nginx/upstreams.d/
%_datadir/grommunio-common/nginx/upstreams.d/grommunio-web.conf
%dir %attr(0770,groweb,groweb) /var/lib/grommunio-web
%dir %attr(0775,groweb,groweb) /var/lib/grommunio-web/tmp
%dir %attr(0775,groweb,groweb) /var/lib/grommunio-web/sqlite-index
%dir %attr(0775,groweb,groweb) /var/lib/grommunio-web/session

%dir %_datadir/%name
%exclude %_datadir/%name/LICENSE.txt
%license LICENSE.txt
%_datadir/%name/*.php
%_datadir/%name/client/
%_datadir/%name/plugins/
%dir %_datadir/%name/server/
%_datadir/%name/server/includes/
%_datadir/%name/server/manifest.dtd
%_datadir/%name/version
%_datadir/%name/cachebuster
%attr(750,root,root) /var/log/grommunio/

%dir %langdir/
%lang(af_ZA) %langdir/af_ZA.UTF-8
%lang(am_ET) %langdir/am_ET.UTF-8
%lang(ar_DZ) %langdir/ar_DZ.UTF-8
%lang(ar_SA) %langdir/ar_SA.UTF-8
%lang(as_IN) %langdir/as_IN.UTF-8
%lang(az_AZ) %langdir/az_AZ.UTF-8
%lang(be_BY) %langdir/be_BY.UTF-8
%lang(bg_BG) %langdir/bg_BG.UTF-8
%lang(bn_BD) %langdir/bn_BD.UTF-8
%lang(bn_IN) %langdir/bn_IN.UTF-8
%lang(bs_BA) %langdir/bs_BA.UTF-8
%lang(ca_ES) %langdir/ca_ES.UTF-8
%lang(ca_ES) %langdir/ca_ES.UTF-8@valencia
%lang(cs_CZ) %langdir/cs_CZ.UTF-8
%lang(cy_GB) %langdir/cy_GB.UTF-8
%lang(da_DK) %langdir/da_DK.UTF-8
%lang(de_CH) %langdir/de_CH.UTF-8
%lang(de_DE) %langdir/de_DE.UTF-8
%lang(el_GR) %langdir/el_GR.UTF-8
%lang(en_GB) %langdir/en_GB.UTF-8
%lang(en_US) %langdir/en_US.UTF-8
%lang(es_ES) %langdir/es_ES.UTF-8
%lang(et_EE) %langdir/et_EE.UTF-8
%lang(eu_ES) %langdir/eu_ES.UTF-8
%lang(fa_IR) %langdir/fa_IR.UTF-8
%lang(fi_FI) %langdir/fi_FI.UTF-8
%lang(fil_PH) %langdir/fil_PH.UTF-8
%lang(fr_FR) %langdir/fr_FR.UTF-8
%lang(ga_IE) %langdir/ga_IE.UTF-8
%lang(gd_GB) %langdir/gd_GB.UTF-8
%lang(gl_ES) %langdir/gl_ES.UTF-8
%lang(gu_IN) %langdir/gu_IN.UTF-8
%lang(he_IL) %langdir/he_IL.UTF-8
%lang(hi_IN) %langdir/hi_IN.UTF-8
%lang(hr_HR) %langdir/hr_HR.UTF-8
%lang(hu_HU) %langdir/hu_HU.UTF-8
%lang(hy_AM) %langdir/hy_AM.UTF-8
%lang(id_ID) %langdir/id_ID.UTF-8
%lang(is_IS) %langdir/is_IS.UTF-8
%lang(it_IT) %langdir/it_IT.UTF-8
%lang(ja_JP) %langdir/ja_JP.UTF-8
%lang(ka_GE) %langdir/ka_GE.UTF-8
%lang(kk_KZ) %langdir/kk_KZ.UTF-8
%lang(km_KH) %langdir/km_KH.UTF-8
%lang(kn_IN) %langdir/kn_IN.UTF-8
%lang(kok_IN) %langdir/kok_IN.UTF-8
%lang(ko_KR) %langdir/ko_KR.UTF-8
%lang(ky_KG) %langdir/ky_KG.UTF-8
%lang(lb_LU) %langdir/lb_LU.UTF-8
%lang(lt_LT) %langdir/lt_LT.UTF-8
%lang(lv_LV) %langdir/lv_LV.UTF-8
%lang(mi_NZ) %langdir/mi_NZ.UTF-8
%lang(mk_MK) %langdir/mk_MK.UTF-8
%lang(ml_IN) %langdir/ml_IN.UTF-8
%lang(mn_MN) %langdir/mn_MN.UTF-8
%lang(mr_IN) %langdir/mr_IN.UTF-8
%lang(ms_MY) %langdir/ms_MY.UTF-8
%lang(mt_MT) %langdir/mt_MT.UTF-8
%lang(nb_NO) %langdir/nb_NO.UTF-8
%lang(ne_NP) %langdir/ne_NP.UTF-8
%lang(nl_NL) %langdir/nl_NL.UTF-8
%lang(nn_NO) %langdir/nn_NO.UTF-8
%lang(or_IN) %langdir/or_IN.UTF-8
%lang(pa_IN) %langdir/pa_IN.UTF-8
%lang(pl_PL) %langdir/pl_PL.UTF-8
%lang(prs_AF) %langdir/prs_AF.UTF-8
%lang(pt_BR) %langdir/pt_BR.UTF-8
%lang(pt_PT) %langdir/pt_PT.UTF-8
%lang(quz_PE) %langdir/quz_PE.UTF-8
%lang(ro_RO) %langdir/ro_RO.UTF-8
%lang(ru_RU) %langdir/ru_RU.UTF-8
%lang(sd_IN) %langdir/sd_IN.UTF-8
%lang(si_LK) %langdir/si_LK.UTF-8
%lang(sk_SK) %langdir/sk_SK.UTF-8
%lang(sl_SI) %langdir/sl_SI.UTF-8
%lang(sq_AL) %langdir/sq_AL.UTF-8
%lang(sr_BA) %langdir/sr_BA.UTF-8
%lang(sr_RS) %langdir/sr_RS.UTF-8
%lang(sr_RS) %langdir/sr_RS.UTF-8@latin
%lang(sv_SE) %langdir/sv_SE.UTF-8
%lang(sw_KE) %langdir/sw_KE.UTF-8
%lang(ta_IN) %langdir/ta_IN.UTF-8
%lang(te_IN) %langdir/te_IN.UTF-8
%lang(th_TH) %langdir/th_TH.UTF-8
%lang(tk_TM) %langdir/tk_TM.UTF-8
%lang(tr_TR) %langdir/tr_TR.UTF-8
%lang(tt_RU) %langdir/tt_RU.UTF-8
%lang(ug_CN) %langdir/ug_CN.UTF-8
%lang(uk_UA) %langdir/uk_UA.UTF-8
%lang(ur_PK) %langdir/ur_PK.UTF-8
%lang(uz_UZ) %langdir/uz_UZ.UTF-8
%lang(vi_VN) %langdir/vi_VN.UTF-8
%lang(zh_CN) %langdir/zh_CN.UTF-8
%lang(zh_TW) %langdir/zh_TW.UTF-8

%changelog
