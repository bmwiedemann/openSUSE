#
# spec file for package python-subliminal
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define oldpython python
Name:           python-subliminal
Version:        2.0.5
Release:        0
Summary:        Python library to search and download subtitles
License:        MIT
URL:            https://github.com/Diaoul/subliminal
Source:         https://files.pythonhosted.org/packages/source/s/subliminal/subliminal-%{version}.tar.gz
# find a way to generate this
Source1:        subliminal.1
# stevedore is not yet unified
BuildRequires:  %{oldpython}-stevedore >= 1.6.0
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module babelfish >= 0.5.4}
BuildRequires:  %{python_module beautifulsoup4 >= 4.4.0}
BuildRequires:  %{python_module chardet >= 2.3.0}
BuildRequires:  %{python_module click >= 4.1}
BuildRequires:  %{python_module devel >= 2.7}
BuildRequires:  %{python_module dogpile.cache >= 0.6.0}
BuildRequires:  %{python_module enzyme >= 0.4.1}
BuildRequires:  %{python_module pysrt >= 1.0.1}
BuildRequires:  %{python_module pyxdg >= 0.25}
BuildRequires:  %{python_module requests >= 2.7.0}
BuildRequires:  %{python_module setuptools  >= 18.0.1}
BuildRequires:  %{python_module six >= 1.9.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-guessit >= 2.0.1
BuildRequires:  python2-html5lib >= 0.999999
BuildRequires:  python2-pbr >= 1.3.0
BuildRequires:  python2-python-dateutil >= 2.2
BuildRequires:  python2-rarfile >= 2.7
BuildRequires:  python3-appdirs >= 1.3
BuildRequires:  python3-stevedore >= 1.6.0
Requires:       python-appdirs >= 1.3
Requires:       python-babelfish >= 0.5.4
Requires:       python-beautifulsoup4 >= 4.4.0
Requires:       python-chardet >= 2.3.0
Requires:       python-click >= 4.1
Requires:       python-dogpile.cache >= 0.6.0
Requires:       python-enzyme >= 0.4.1
Requires:       python-guessit >= 2.0.1
Requires:       python-pysrt >= 1.0.1
Requires:       python-pytz >= 2012c
Requires:       python-pyxdg >= 0.25
Requires:       python-rarfile >= 2.7
Requires:       python-requests >= 2.7.0
Requires:       python-six >= 1.9.0
Recommends:     python-colorlog >= 2.6.0
BuildArch:      noarch
%ifpython2
# Stevedore is not yet unified
Requires:       %{oldpython}-stevedore >= 1.6.0
Requires:       python-futures >= 3.0
Requires:       python-html5lib >= 0.999999
Requires:       python-pbr >= 1.3.0
Requires:       python-python-dateutil >= 2.2
%endif
%ifpython3
Requires:       python-dbm
Requires:       python3-stevedore >= 1.6.0
%endif
%ifpython3
Provides:       subliminal = %{version}
Obsoletes:      subliminal < %{version}
%endif
%python_subpackages

%description
Subliminal is a python library to search and download subtitles.
It comes with an easy to use CLI suitable for direct use or cron jobs.

%prep
%setup -q -n subliminal-%{version}

%build
%python_build

%install
%python_install
mkdir -p %{buildroot}/%{_mandir}/man1
install -m 644 %{SOURCE1} -t %{buildroot}/%{_mandir}/man1
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc HISTORY.rst README.rst
%python3_only %{_bindir}/subliminal
%python3_only %{_mandir}/man1/subliminal.1%{ext_man}
%{python_sitelib}/subliminal
%{python_sitelib}/subliminal-%{version}-py%{python_version}.egg-info

%changelog
