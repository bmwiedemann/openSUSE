#
# spec file for package desktop-translations
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


Name:           desktop-translations
Version:        84.87.20230128.350400f
Release:        0
Summary:        Desktop Files Translations
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/openSUSE/desktop-file-translations
Source0:        desktop-file-translations-%{version}.tar.xz
Supplements:    bundle-lang-other
Supplements:    gtk2
Supplements:    gtk3
Supplements:    kdelibs3
Supplements:    libkde4
Supplements:    plasma5-desktop
Supplements:    yast2-control-center
Provides:       locale(af;ar;bg;be;bn;bs;ca;cs;cy;da;de;el;en_GB;eo;es;et;fi;fr;gl;gu;he;hi;hr;hu;id;it;ja;ka;kab;km;ko;lo;lt;mk;mr;nb;nl;pa;pl;pt;ro;ru;si;sk;sl;sr;sr@Latn;sv;ta;tr;uk;vi;wa;xh;zh_CN;zh_TW;zu)
BuildRequires:  gettext-runtime
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package provides the translations for installed desktop files.

%prep
%setup -q -c %{name}

%build
mv desktop-file-translations-%{version}/* .
./50-tools/build-entries-po.sh

%install
pushd po
for lang in *; do
  if test "$lang" = "nb_no"; then
    continue
  fi
  if test -f $lang; then
	rm $lang
  else
    mkdir -p %{buildroot}%{_datadir}/locale/${lang}/LC_MESSAGES
    for f in ${lang}/*.po; do
       msgfmt -o %{buildroot}%{_datadir}/locale/${lang}/LC_MESSAGES/desktop_translations.mo $f
       msgunfmt --no-wrap %{buildroot}%{_datadir}/locale/${lang}/LC_MESSAGES/desktop_translations.mo | \
          grep -v '^"[A-Z][^ ]*: ' | grep '[^\][\]n"' && exit 1
    done
  fi
done
popd

for lang in *; do
    if [ -e "${lang}/polkitaction.po" ]; then
	msgfmt -o "%{buildroot}%{_datadir}/locale/${lang}/LC_MESSAGES/polkit-action-distro-translations.mo" "${lang}/polkitaction.po"
    fi
done

%find_lang %{name} --all-name

%files -f %{name}.lang
%defattr(-,root,root)

%changelog
