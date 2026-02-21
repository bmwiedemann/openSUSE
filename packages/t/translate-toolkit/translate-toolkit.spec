#
# spec file for package translate-toolkit
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%bcond_with doc
%endif 
%if "%{flavor}" == "man+doc"
%define psuffix -man
%bcond_with test
%bcond_without doc
%endif
%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with test
%bcond_with doc
%endif
%define modname translate_toolkit
%define pkgname translate-toolkit
%bcond_without libalternatives

%define binaries_and_manpages %{shrink:\
    pretranslate poclean pocompile poconflicts podebug pofilter pogrep pomerge porestructure posegment poswap poterminology \
    android2po arb2po asciidoc2po csv2po csv2tbx dtd2po flatxml2po fluent2po html2po ical2po idml2po ini2po json2po \
    moz2po mozfunny2prop mozlang2po odf2xliff oo2po oo2xliff php2po phppo2pypo \
    po2asciidoc po2csv po2dtd po2flatxml po2html po2ical po2idml po2ini po2json po2moz po2mozlang po2odf po2oo \
    po2php po2prop po2rc po2resx po2symb po2tiki po2tmx po2toml po2ts po2txt po2web2py \
    po2wordfast po2xliff po2yaml pot2po prop2po pypo2phppo rc2po resx2po symb2po \
    tbx2po tiki2po toml2po ts2po txt2po web2py2po xliff2odf xliff2oo xliff2po yaml2po}
%define binaries %{shrink: %binaries_and_manpages\
    pocommentclean pocompendium pocount pomigrate2 popuretext poreencode posplit prop2mozfunny \
    pydiff junitmsgfmt md2po po2md po2sub sub2po}
%define manpages translatetoolkit %binaries_and_manpages

Name:           translate-toolkit%{psuffix}
Version:        3.19.1
Release:        0
Summary:        Tools and API to assist with translation and software localization
License:        GPL-2.0-or-later
URL:            https://toolkit.translatehouse.org/
Source:         https://github.com/translate/translate/archive/refs/tags/%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module cheroot >= 10}
BuildRequires:  %{python_module iniparse >= 0.5}
BuildRequires:  %{python_module lxml >= 5.2.0}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module phply >= 1.2.6}
BuildRequires:  %{python_module ruamel.yaml >= 0.18.0}
BuildRequires:  %{python_module setuptools >= 78.0.2}
BuildRequires:  %{python_module vobject >= 0.9.9}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gettext-runtime
BuildRequires:  git-core
BuildRequires:  iso-codes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       gettext-runtime
Requires:       python
Requires:       python-tomlkit
Requires:       python-unicode-segmentation-rs
Requires:       python-lxml >= 5.2.0
# The following are for the full experience of translate-toolkit
Recommends:     %{name}-doc
Recommends:     %{name}-man
Recommends:     gaupol
Recommends:     iso-codes
Recommends:     python-Levenshtein >= 0.21.0
Recommends:     python-aeidon >= 1.14.1
Recommends:     python-beautifulsoup4 >= 4.13.0
Recommends:     python-charset-normalizer >= 3.4.0
Recommends:     python-cheroot >= 10
Recommends:     python-fluent.syntax >= 0.19.0
Recommends:     python-iniparse >= 0.5
Recommends:     python-mistletoe >= 1.4.0
Recommends:     python-phply >= 1.2.6
Recommends:     python-pyenchant >= 3.2.2
Recommends:     python-pyparsing >= 3.2.0
Recommends:     python-ruamel.yaml >= 0.18.0
Recommends:     python-vobject >= 0.9.9
%if %{without test} && %{without doc} && ("%{python_flavor}" == "python3" || "%{?python_provides}" == "python3")
Provides:       translate-toolkit = %{version}-%{release}
Obsoletes:      translate-toolkit < %{version}-%{release}
%endif
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Levenshtein >= 0.21.0}
BuildRequires:  %{python_module aeidon >= 1.14.1}
BuildRequires:  %{python_module beautifulsoup4 >= 4.13.0}
BuildRequires:  %{python_module charset-normalizer >= 3.3.2}
BuildRequires:  %{python_module fluent.syntax >= 0.19.0}
BuildRequires:  %{python_module mistletoe >= 1.4.0}
BuildRequires:  %{python_module pyenchant >= 3.2.2}
BuildRequires:  %{python_module pyparsing >= 3.2.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module translate-toolkit = %{version}}
BuildRequires:  %{python_module xml}
BuildRequires:  %{python_module syrupy}
BuildRequires:  gaupol
%endif
%if %{with doc}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module fluent.syntax >= 0.19.0}
BuildRequires:  %{python_module furo}
BuildRequires:  %{python_module sphinxcontrib-copybutton}
BuildRequires:  %{python_module sphinxext-opengraph}
BuildRequires:  %{python_module translate-toolkit = %{version}}
Requires:       %{pkgname} = %{version}
Supplements:    %{pkgname} = %{version}
%endif
%python_subpackages

%if "%{flavor}" == "man+doc"
%description
The %{pkgname}-man package contains manual pages for %{pkgname}.

%package -n %{pkgname}-doc
Summary:        Tools and API to assist with translation and software localization -- HTML docs
Requires:       %{pkgname} = %{version}
BuildArch:      noarch

%description -n %{pkgname}-doc
The %{pkgname}-doc package contains Translate Toolkit documentation in HTML format.

%package -n %{pkgname}-devel-doc
Summary:        Tools and API to assist with translation and software localization -- API docs
Requires:       %{pkgname} = %{version}
Requires:       %{pkgname}-doc = %{version}
Provides:       %{pkgname}-devel = %{version}
Obsoletes:      %{pkgname}-devel < %{version}
BuildArch:      noarch

%description -n %{pkgname}-devel-doc
The %{pkgname}-devel-doc package contains Translate Toolkit API documentation for developers wishing to build new tools for the
toolkit or to use the libraries in other localization tools.

%else

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
%endif

%prep
%setup -q -n translate-%{version}
%autopatch -p1

#Fix for shebang errors:
for lib in translate/{*.py,*/*.py,*/*/*.py}; do
 sed -i '\|%{_bindir}/env |d' $lib
done

find . -name jquery.js -exec dos2unix '{}' \;

%build
%if !%{with test}
%if !%{with doc}
%pyproject_wheel

%else

# build docs
pushd docs
# Can't use parallel build here!
%make_build SPHINXBUILD=sphinx-build -j1 man html
#no hidden files
find _build -name '.?*' -delete
popd
%endif
%endif

%install
%if !%{with test}
%if !%{with doc}
%pyproject_install

%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Prepare alternatives for binaries
for binary in %{binaries} ; do
%python_clone -a %{buildroot}%{_bindir}/$binary
done

%else

# create manpages
mkdir -p %{buildroot}%{_mandir}/man1
for program in %{binaries}; do
    MPAGE="%{buildroot}%{_mandir}/man1/$program.1"
    LC_ALL=C PYTHONPATH=. %{_bindir}/$program --manpage > "$MPAGE" || rm -f "$MPAGE"
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

# Prepare alternatives for manpages
for mpage in %{manpages} ; do
%python_clone -a %{buildroot}%{_mandir}/man1/$mpage.1
done

%endif
%endif

%check
%if %{with test}
rm -v tests/translate/storage/test_fluent.py
%pytest
%endif

%if !%{with test}
%if !%{with doc}

%pre
%python_libalternatives_reset_alternative pretranslate

%files %{python_files}
%license COPYING
%doc README.rst
%{lua: for b in string.gmatch(rpm.expand("%binaries"),"%S+") do print(rpm.expand("%python_alternative %{_bindir}/" .. b) .. "\n") end}
%{python_sitelib}/translate
%{python_sitelib}/translate_toolkit-%{version}.dist-info

%else

%pre
%python_libalternatives_reset_alternative translatetoolkit.1%{?ext_man}

%files %{python_files}
%license COPYING
%doc README.rst
%{lua: for m in string.gmatch(rpm.expand("%manpages"),"%S+") do print(rpm.expand("%python_alternative %{_mandir}/man1/" .. m .. ".1") .. "\n") end}
# needed because we are building manpages separately
%if %{with libalternatives}
%{lua: for m in string.gmatch(rpm.expand("%manpages"),"%S+") do print(rpm.expand("%dir %{_datadir}/libalternatives/" .. m .. "") .. "\n") end}
%{lua: for m in string.gmatch(rpm.expand("%manpages"),"%S+") do print(rpm.expand("%{_datadir}/libalternatives/" .. m .. "/*%{python_version_nodots}.conf") .. "\n") end}
%endif

%files -n %{pkgname}-doc
%dir %{_defaultdocdir}/%{modname}
%doc %{_defaultdocdir}/%{modname}/html/
%exclude %{_defaultdocdir}/%{modname}/html/api
%exclude %{_defaultdocdir}/%{modname}/html/_sources

%files -n %{pkgname}-devel-doc
%doc %{_defaultdocdir}/%{modname}/html/api
%doc %{_defaultdocdir}/%{modname}/html/_sources
%endif
%endif

%changelog
