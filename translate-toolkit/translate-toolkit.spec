#
# spec file for package translate-toolkit
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


Name:           translate-toolkit
Version:        2.4.0
Release:        0
Summary:        Tools and API to assist with translation and software localization
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            http://toolkit.translatehouse.org/
Source:         https://github.com/translate/translate/releases/download/%{version}/%{name}-%{version}.tar.gz
# Repacked https://github.com/translate/sphinx-themes ; no commits since 2013
# Often not included in the release tag so just ship it
Source1:        sphinx-themes.tar.xz
Patch0:         sphinx-intersphinx.patch
Patch2:         xliff-xsd-no-network.patch
BuildRequires:  fdupes
BuildRequires:  gettext-runtime
BuildRequires:  git-core
BuildRequires:  iso-codes
BuildRequires:  python3-Babel
BuildRequires:  python3-Levenshtein
BuildRequires:  python3-Sphinx
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-cheroot
BuildRequires:  python3-iniparse
BuildRequires:  python3-l20n
BuildRequires:  python3-lxml >= 3.5.0
BuildRequires:  python3-phply
BuildRequires:  python3-pycountry >= 18.12.8
BuildRequires:  python3-pyenchant
BuildRequires:  python3-pytest
BuildRequires:  python3-ruamel.yaml
BuildRequires:  python3-six >= 1.11.0
BuildRequires:  python3-vobject
BuildRequires:  python3-xml
BuildRequires:  subversion
Requires:       gettext-runtime
Requires:       python3-lxml
Requires:       python3-pycountry >= 18.12.8
Requires:       python3-pyenchant
Requires:       python3-setuptools
Requires:       python3-six >= 1.11.0
# The following are for the full experience of translate-toolkit
Recommends:     gaupol
Recommends:     iso-codes
Recommends:     python3-Levenshtein
Recommends:     python3-aeidon
Recommends:     python3-chardet
Recommends:     python3-cheroot
Recommends:     python3-iniparse
Recommends:     python3-l20n
Recommends:     python3-phply
Recommends:     python3-pycountry
Recommends:     python3-ruamel.yaml
Recommends:     python3-vobject
Provides:       python3-translate-toolkit = %{version}
BuildArch:      noarch

%description
The Translate Toolkit is a set of software and documentation designed to help
make the lives of localizers both more productive and less frustrating.

The software includes programs to convert localization formats to the common
PO, and emerging XLIFF format.  There are also programs to check and manage PO
and XLIFF files.  Online documentation includes guides on using the tools,
running a localization project and how to localize various projects from
OpenOffice.org to Mozilla.

At its core the software contains a set of classes for handling various
localization storage formats: DTD, properties, OpenOffice.org GSI/SDF,
CSV, MO, Qt .ts, TMX, TBX, WordFast txt, Gettext .mo, Windows RC, and
of course PO and XLIFF.  It also provides scripts to convert between
these formats.

Also part of the Toolkit are Python programs to create word counts, merge
translations and perform various checks on translation files.

%package devel-doc
Summary:        Tools and API to assist with translation and software localization
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
Obsoletes:      %{name}-devel < %{version}
BuildArch:      noarch

%description devel-doc
The %{name}-devel-doc package contains Translate Toolkit API documentation for developers wishing to build new tools for the
toolkit or to use the libraries in other localization tools.

%prep
%setup -q
%autopatch -p1

pushd docs/_themes
tar -xJf %{SOURCE1} --strip 1
popd

sed -i 296"s|'share'|'translate/share'|" setup.py

#Fix for shebang errors:
for lib in translate/{*.py,*/*.py,*/*/*.py}; do
 sed -i '\|%{_bindir}/env |d' $lib
done

%build
python3 setup.py build
pushd docs
# Can't use parallel build here!
make -j1 html man
#no hidden files
find _build -name '.?*' -delete
popd

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

# create manpages
mkdir -p %{buildroot}/%{_mandir}/man1
for program in %{buildroot}/%{_bindir}/*; do
    case $(basename $program) in
      pocompendium|poen|pomigrate2|popuretext|poreencode|posplit|pocount|poglossary|lookupclient.py|tmserver|build_tmdb)
        ;;
      *)
        LC_ALL=C PYTHONPATH=. $program --manpage \
          >  %{buildroot}/%{_mandir}/man1/$(basename $program).1 \
          || rm -f %{buildroot}/%{_mandir}/man1/$(basename $program).1
        ;;
    esac
done
install -m 644 docs/_build/man/* %{buildroot}/%{_mandir}/man1/

# move documentation files to datadir
install -d -m 755 %{buildroot}%{_defaultdocdir}/%{name}
mv %{buildroot}%{python3_sitelib}/translate/docs/_build/html %{buildroot}%{_defaultdocdir}/%{name}
rm -rf %{buildroot}%{python3_sitelib}/translate/docs
rm -rf %{buildroot}/home/abuild/.local/lib/python%{python3_version}/site-packages/

# create symlinks for man pages
%fdupes -s %{buildroot}/%{_mandir}
# create hardlinks for the rest
%fdupes %{buildroot}

%check
export PATH=$PATH:%{buildroot}%{_bindir}
PYTHONPATH=%{buildroot}%{python3_sitelib} python3 -m pytest -v

%files
%{_defaultdocdir}/%{name}/html/
%exclude %{_defaultdocdir}/%{name}/html/api
%exclude %{_defaultdocdir}/%{name}/html/_sources
%license COPYING
%doc README.rst
%{_bindir}/*
%{_mandir}/man1/*
%{python3_sitelib}/translate
%{python3_sitelib}/translate_toolkit-%{version}-*.egg-info

%files devel-doc
%doc %{_defaultdocdir}/%{name}/html/api
%doc %{_defaultdocdir}/%{name}/html/_sources

%changelog
