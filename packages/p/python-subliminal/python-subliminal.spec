#
# spec file for package python-subliminal
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-subliminal
Version:        2.2.1
Release:        0
Summary:        Python library to search and download subtitles
License:        MIT
URL:            https://github.com/Diaoul/subliminal
Source:         https://files.pythonhosted.org/packages/source/s/subliminal/subliminal-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools  >= 18.0.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-babelfish >= 0.6.1
Requires:       python-beautifulsoup4 >= 4.4.0
Requires:       python-chardet >= 5.0
Requires:       python-click >= 8.0
Requires:       python-click-option-group >= 0.5.6
Requires:       python-dogpile.cache >= 1.0
Requires:       python-enzyme >= 0.5.0
Requires:       python-guessit >= 3.0.0
Requires:       python-platformdirs >= 3
Requires:       python-pysubs2 >= 1.7
Requires:       python-rarfile >= 2.7
Requires:       python-requests >= 2.7.0
Requires:       python-srt >= 3.5
Requires:       python-stevedore >= 3.0
Requires:       python-tomli >= 2
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-colorlog >= 2.6.0
Provides:       subliminal = %{version}
Obsoletes:      subliminal < %{version}
BuildArch:      noarch
%python_subpackages

%description
Subliminal is a python library to search and download subtitles.
It comes with an easy to use CLI suitable for direct use or cron jobs.

%prep
%autosetup -n subliminal-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/subliminal
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check

%post
%python_install_alternative subliminal

%postun
%python_uninstall_alternative subliminal

%files %{python_files}
%license LICENSE
%doc HISTORY.rst README.rst
%python_alternative %{_bindir}/subliminal
%{python_sitelib}/subliminal
%{python_sitelib}/subliminal-%{version}.dist-info

%changelog
