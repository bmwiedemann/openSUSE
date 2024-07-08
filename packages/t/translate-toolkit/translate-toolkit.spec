#
# spec file for package translate-toolkit
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define modname translate_toolkit

%define binaries_and_manpages %{shrink:\
    poclean pocompile poconflicts podebug pofilter pogrep pomerge porestructure posegment poswap poterminology \
    pretranslate \
    android2po csv2po csv2tbx dtd2po flatxml2po html2po ical2po idml2po ini2po json2po \
    moz2po mozfunny2prop mozlang2po odf2xliff oo2po oo2xliff php2po phppo2pypo \
    po2csv po2dtd po2flatxml po2html po2ical po2idml po2ini po2json po2moz po2mozlang po2oo \
    po2php po2prop po2rc po2resx po2sub po2symb po2tiki po2tmx po2ts po2txt po2web2py \
    po2wordfast po2xliff po2yaml pot2po prop2po pypo2phppo rc2po resx2po sub2po symb2po \
    tbx2po tiki2po ts2po txt2po web2py2po xliff2odf xliff2oo xliff2po yaml2po}
%define binaries %{shrink: %binaries_and_manpages\
    pocommentclean pocompendium pocount pomigrate2 popuretext poreencode posplit prop2mozfunny \
    build_tmdb pydiff tmserver junitmsgfmt md2po po2md}
%define manpages translatetoolkit %binaries_and_manpages

Name:           translate-toolkit%{psuffix}
Version:        3.13.1
Release:        0
Summary:        Tools and API to assist with translation and software localization
License:        GPL-2.0-or-later
URL:            https://toolkit.translatehouse.org/
Source:         https://files.pythonhosted.org/packages/source/t/%{modname}/%{modname}-%{version}.tar.gz
Patch0:         xliff-xsd-no-network.patch
Patch1:         sphinx-intersphinx.patch
BuildRequires:  %{python_module Levenshtein >= 0.12}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module sphinx-bootstrap-theme}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module beautifulsoup4 >= 4.3}
# extra modules here are needed for manpages
BuildRequires:  %{python_module cheroot >= 9}
BuildRequires:  %{python_module iniparse >= 0.5}
BuildRequires:  %{python_module lxml >= 4.6.3}
BuildRequires:  %{python_module phply >= 1.2.5}
BuildRequires:  %{python_module ruamel.yaml >= 0.17.21}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  %{python_module setuptools_scm >= 6.2}
BuildRequires:  %{python_module vobject >= 0.9.6.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gettext-runtime
BuildRequires:  git-core
BuildRequires:  iso-codes
BuildRequires:  python-rpm-macros
Requires:       gettext-runtime
Requires:       python
Requires:       python-lxml >= 4.6.3
Requires(post): update-alternatives
Requires(postun): update-alternatives
# The following are for the full experience of translate-toolkit
Recommends:     %{name}-doc
Recommends:     gaupol
Recommends:     iso-codes
Recommends:     python-Levenshtein >= 0.12
Recommends:     python-aeidon >= 1.13
Recommends:     python-beautifulsoup4 >= 4.3
Recommends:     python-charset-normalizer >= 3.3.2
Recommends:     python-cheroot >= 10
Recommends:     python-iniparse >= 0.5
Recommends:     python-mistletoe >= 1.2.1
Recommends:     python-phply >= 1.2.6
Recommends:     python-pyenchant >= 3.2.2
Recommends:     python-pyparsing >= 3.1.1
Recommends:     python-ruamel.yaml >= 0.18.5
Recommends:     python-vobject >= 0.9.6.1
%if "%{python_flavor}" == "python3" || "%{?python_provides}" == "python3"
Provides:       translate-toolkit = %{version}-%{release}
Obsoletes:      translate-toolkit < %{version}-%{release}
%endif
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module aeidon >= 1.13}
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module mistletoe >= 1.2.1}
BuildRequires:  %{python_module pyenchant >= 3.2.2}
BuildRequires:  %{python_module pyparsing >= 3.1.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module translate-toolkit = %{version}}
BuildRequires:  %{python_module xml}
BuildRequires:  %{python_module syrupy}
BuildRequires:  gaupol
%endif
%python_subpackages

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

%package -n %{name}-doc
Summary:        Tools and API to assist with translation and software localization -- HTML docs
Requires:       %{name} = %{version}
BuildArch:      noarch

%description -n %{name}-doc
The %{name}-doc package contains Translate Toolkit documentation in HTML format.

%package -n %{name}-devel-doc
Summary:        Tools and API to assist with translation and software localization -- API docs
Requires:       %{name} = %{version}
Requires:       %{name}-doc = %{version}
Provides:       %{name}-devel = %{version}
Obsoletes:      %{name}-devel < %{version}
BuildArch:      noarch

%description -n %{name}-devel-doc
The %{name}-devel-doc package contains Translate Toolkit API documentation for developers wishing to build new tools for the
toolkit or to use the libraries in other localization tools.

%prep
%setup -q -n %{modname}-%{version}
%autopatch -p1

sed -i 296"s|'share'|'translate/share'|" setup.py

#Fix for shebang errors:
for lib in translate/{*.py,*/*.py,*/*/*.py}; do
 sed -i '\|%{_bindir}/env |d' $lib
done

find . -name jquery.js -exec dos2unix '{}' \;

%build
%if !%{with test}
%pyproject_wheel

pushd docs
# Can't use parallel build here!
%make_build -j1 html man
#no hidden files
find _build -name '.?*' -delete
popd
%endif

%install
%if !%{with test}
%pyproject_install

# create manpages
mkdir -p %{buildroot}%{_mandir}/man1
for program in %{buildroot}%{_bindir}/*; do
    MPAGE="%{buildroot}%{_mandir}/man1/$(basename $program).1"
    LC_ALL=C PYTHONPATH=. $program --manpage > "$MPAGE" || rm -f "$MPAGE"
done
install -m 644 docs/_build/man/* %{buildroot}%{_mandir}/man1/

# move documentation files to datadir, use default flavor version for common
install -d -m 755 %{buildroot}%{_defaultdocdir}/%{modname}
mv docs/_build/html %{buildroot}%{_defaultdocdir}/%{modname}
%{python_expand rm -rf %{buildroot}%{$python_sitelib}/translate/docs
rm -rf %{buildroot}home/abuild/.local/lib/python%{$python_version}/site-packages/
}

# create symlinks for man pages
%fdupes -s %{buildroot}%{_mandir}
# create hardlinks for the rest
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Prepare alternatives
for mpage in %{manpages} ; do
%python_clone -a %{buildroot}%{_mandir}/man1/$mpage.1
done
for binary in %{binaries} ; do
%python_clone -a %{buildroot}%{_bindir}/$binary
done
%endif

%check
%if %{with test}
rm -v tests/translate/storage/test_fluent.py
%pytest
%endif

%post
%python_install_alternative %{lua: for m in string.gmatch(rpm.expand("%manpages"),"%S+") do print(m .. ".1 ") end} %binaries

%postun
%python_uninstall_alternative translatetoolkit.1%{?ext_man}

%if !%{with test}
%files %{python_files}
%license COPYING
%doc README.rst
%{lua: for b in string.gmatch(rpm.expand("%binaries"),"%S+") do print(rpm.expand("%python_alternative %{_bindir}/" .. b) .. "\n") end}
%{lua: for m in string.gmatch(rpm.expand("%manpages"),"%S+") do print(rpm.expand("%python_alternative %{_mandir}/man1/" .. m .. ".1") .. "\n") end}
%{python_sitelib}/translate
%{python_sitelib}/translate_toolkit-%{version}.dist-info

%files -n %{name}-doc
%dir %{_defaultdocdir}/%{modname}
%doc %{_defaultdocdir}/%{modname}/html/
%exclude %{_defaultdocdir}/%{modname}/html/api
%exclude %{_defaultdocdir}/%{modname}/html/_sources

%files -n %{name}-devel-doc
%doc %{_defaultdocdir}/%{modname}/html/api
%doc %{_defaultdocdir}/%{modname}/html/_sources
%endif

%changelog
