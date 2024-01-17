#
# spec file for package eric
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2010-2023 LISA GmbH, Bingen, Germany
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


%define distname eric7

# install option to install many tools as stand alone applications
%bcond_with tools

Name:           eric
Version:        23.4.2
Release:        0
Summary:        Python IDE based on Qt6
License:        GPL-3.0-or-later
Group:          Development/Tools/IDE
URL:            https://eric-ide.python-projects.org/
Source:         https://sourceforge.net/projects/eric-ide/files/%{distname}/stable/%{version}/%{distname}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  python3-EditorConfig
BuildRequires:  python3-qscintilla-qt6
BuildRequires:  python3-qt6
BuildRequires:  python3-qtcharts-qt6
BuildRequires:  python3-qtwebengine-qt6
BuildRequires:  python3-xml
BuildRequires:  update-desktop-files
Requires:       python3-EditorConfig
Requires:       python3-Pygments
Requires:       python3-asttokens
Requires:       python3-black
Requires:       python3-coverage
Requires:       python3-isort
Requires:       python3-jedi
Requires:       python3-packaging
Requires:       python3-parso
Requires:       python3-qscintilla-qt6
Requires:       python3-qt6
Requires:       python3-qtcharts-qt6
Requires:       python3-qtwebengine-qt6
Requires:       python3-semver
Requires:       python3-tomlkit
Requires:       python3-trove-classifiers
Requires:       python3-xml
Requires:       qt6-sql-sqlite
Recommends:     %{name}-api = %{version}
Recommends:     python3-Markdown
Recommends:     python3-Send2Trash
Recommends:     python3-chardet
Recommends:     python3-cx_Freeze
# these are required as of install.py:doDependancyChecks
# until we provide those, just recommend them
Recommends:     python3-cyclonedx-bom
Recommends:     python3-cyclonedx-python-lib
Recommends:     python3-doc
Recommends:     python3-docutils
Recommends:     python3-pyenchant
Recommends:     python3-pylint >= 0.18.0
Recommends:     python3-pysvn >= 1.7.0
Recommends:     python3-pyyaml
Recommends:     python3-rope >= 0.9.2
Recommends:     python3-wheel
Recommends:     qt6-sql-mysql
Recommends:     qt6-sql-postgresql
Provides:       python-eric5 = %{version}
Obsoletes:      python-eric5 < %{version}
Provides:       python-eric6 = %{version}
Obsoletes:      python-eric6 < %{version}
Provides:       eric5 = %{version}
Obsoletes:      eric5 < %{version}
Provides:       eric6 = %{version}
Obsoletes:      eric6 < %{version}
BuildArch:      noarch

%description
Eric is a Python and Ruby editor and IDE, written in Python. It is
based on the Qt GUI toolkit and integrates the Scintilla editor
control.

%package api
Summary:        API files for eric6
Group:          Development/Tools/IDE
Provides:       python-eric5-api = %{version}
Obsoletes:      python-eric5-api < %{version}
Provides:       python-eric6-api = %{version}
Obsoletes:      python-eric6-api < %{version}
Provides:       eric5-api = %{version}
Obsoletes:      eric5-api < %{version}
Provides:       eric6-api = %{version}
Obsoletes:      eric6-api < %{version}

%description api
This package provides API files for eric6.
If both python-eric6 and python3-eric6 packages are installed then only one
python-eric6-api or python3-eric6-api is needed.

%prep
%setup -q -n %{distname}-%{version}

find . -name \*.py -exec sed -i -e '/^#!\/usr\/bin.*python/d' '{}' \;

%build
# nothing here

%install
%if %{with tools}
    python3 install.py -b %{_bindir} -d %{python3_sitelib} -i %{buildroot} --with-tools --no-info
%else
    python3 install.py -b %{_bindir} -d %{python3_sitelib} -i %{buildroot} --no-info
%endif
%fdupes %{buildroot}%{python3_sitelib}
ln -sf %{distname}_ide %{buildroot}%{_bindir}/%{distname}
ln -sf %{distname}_ide %{buildroot}%{_bindir}/%{name}

%files
%license eric/docs/LICENSE.txt
%doc eric/docs/README*.rst eric/docs/THANKS eric/docs/changelog.md eric/docs/%{distname}-plugin.odt
%{_bindir}/*
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/%{distname}.appdata.xml
%{_datadir}/applications/%{distname}_ide.desktop
%{_datadir}/applications/%{distname}_browser.desktop
%{_datadir}/icons/eric.png
%{_datadir}/icons/ericWeb.png
%{_datadir}/icons/hicolor/*/apps/eric.png
%{_datadir}/icons/hicolor/*/apps/ericWeb.png
%{python3_sitelib}/

%files api
%license eric/docs/LICENSE.txt
#%%dir %{_datadir}/qt6/qsci/api/
%{_datadir}/qt6/qsci/api/

%changelog
