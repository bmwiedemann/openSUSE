#
# spec file for package fonts-config
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           fonts-config
Version:        20200609+git0.42e2b1b
Release:        0
Summary:        Script to configure fonts for X Windows and other applications
# MIT for infinality
License:        GPL-2.0-or-later AND MIT
Group:          System/X11/Fonts
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fontconfig
BuildRequires:  fontpackages-devel
Requires(pre):  %fillup_prereq
%reconfigure_fonts_prereq
Requires:       fontconfig
Requires:       gawk
Requires:       perl(English)
Recommends:     mkfontscale
Recommends:     mkfontdir
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A script to configure fonts for X Windows and other applications.

fonts-config is usually called automatically when a package containing
fonts is installed, upgraded or removed. But it can also be executed
directly, which is mainly useful to debug it (use the --debug flag).

%prep
%setup

%build
# empty configuration now, should be filled after fonts-config call
cp 99-example.conf 10-rendering-options.conf
# empty configuration now, can be filled after fonts-config call
cp 99-example.conf 58-family-prefer-local.conf

%install
mkdir -p %{buildroot}/sbin/conf.d
mkdir -p %{buildroot}%{_prefix}/sbin
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}/%{_mandir}/man1
mkdir -p %{buildroot}/%{_docdir}/%{name}/infinality
mkdir -p %{buildroot}%{_fillupdir}
install -m 755 fonts-config %{buildroot}%{_prefix}/sbin
install -m 644 sysconfig.fonts-config \
  %{buildroot}%{_fillupdir}/
install -m 644 fontconfig.SUSE.properties.template %{buildroot}%{_datadir}/fonts-config
pod2man --section 1 --center=" " fonts-config > \
  %{buildroot}/%{_mandir}/man1/fonts-config.1
#
install -m 644 10-rendering-options.conf.template %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_fontsconfavaildir}
# following two conf files can not be under /usr/share/fonts-config
# as they are changed during installation [bnc#882029 (internal)]
mkdir -p %{buildroot}%{_fontsconfddir}
for conf in     10-rendering-options.conf \
                58-family-prefer-local.conf; do
  install -m 644 $conf %{buildroot}%{_fontsconfddir}
done
#
for conf in 	10-group-tt-hinted-fonts.conf \
		10-group-tt-non-hinted-fonts.conf \
		11-base-rendering.conf \
		12-tt-monospace-rendering.conf \
		13-selective-rendering.conf \
		13-selective-rendering-ipa.conf \
    21-emoji-rendering.conf \
    31-metric-aliases-bw.conf \
    32-emoji-reject.conf \
    32-symbol-substitution.conf \
		49-family-default.conf \
		59-family-prefer-lang-specific.conf \
		60-family-prefer.conf \
		61-wine-aliases.conf \
		70-reject.conf; do
  install -m 644 $conf %{buildroot}%{_datadir}/%{name}/conf.avail/
  %link_avail_to_system_fontsconf $conf
done

%post
if [ -f %{_sysconfdir}/sysconfig/fonts-config ]; then
  update=$(grep "^FORCE_MODIFY_DEFAULT_FONT_SETTINGS_IN_NEXT_UPDATE=" %{_sysconfdir}/sysconfig/fonts-config | sed -e 's/.*="//;s/"$//')
  if [ -z "$update" -o "$update" = "yes" ]; then
     echo "Updating default font settings..."
     force_hintstyle=$(grep "^FORCE_HINTSTYLE=" /usr/share/fillup-templates/sysconfig.fonts-config | sed -e 's/.*=//')
     use_lcdfilter=$(grep "^USE_LCDFILTER=" /usr/share/fillup-templates/sysconfig.fonts-config | sed -e 's/.*=//')
     use_rgba=$(grep "^USE_RGBA=" /usr/share/fillup-templates/sysconfig.fonts-config | sed -e 's/.*=//')
     if [ ! -f %{_sysconfdir}/sysconfig/fonts-config.rpmsave ]; then
         cp %{_sysconfdir}/sysconfig/fonts-config %{_sysconfdir}/sysconfig/fonts-config.rpmsave
     fi
     sed -i -e '14,16s/^## Default:     none$/## Default:     '"$force_hintstyle"/ \
            -e 's/^FORCE_HINTSTYLE="none"$/FORCE_HINTSTYLE='"$force_hintstyle"/ \
            -e 's/^## Default:     lcdnone$/## Default:     '"$use_lcdfilter"/ \
            -e 's/^USE_LCDFILTER="lcdnone"$/USE_LCDFILTER='"$use_lcdfilter"/ \
            -e '76,78s/^## Default:     none$/## Default:     '"$use_rgba"/ \
            -e 's/^USE_RGBA="none"$/USE_RGBA='"$use_rgba"/ \
               %{_sysconfdir}/sysconfig/fonts-config
  fi
fi
# Note that the above code should run before fillup merges the (maybe new)
# FORCE_MODIFY_DEFAULT_FONT_SETTINGS_IN_NEXT_UPDATE variable
# in a system being updated.
%{fillup_only -n fonts-config}
%reconfigure_fonts_post -c
exit 0

%postun
%reconfigure_fonts_postun -c

%posttrans
%reconfigure_fonts_posttrans

%files
%defattr(-,root,root)
%dir %{_datadir}/fonts-config
%files_fontsconf_availdir
%{_sbindir}/fonts-config
%{_datadir}/fonts-config/*.template
%{_mandir}/man1/fonts-config.1.gz
%{_docdir}/%{name}
%{_fillupdir}/sysconfig.fonts-config
%{_fontsconfavaildir}/*.conf
%config %{_fontsconfddir}/*.conf

%changelog
