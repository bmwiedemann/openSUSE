#
# spec file for package python-guessit
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%if 0%{?suse_version} > 1500
%bcond_without test
%bcond_without libalternatives
%else
%bcond_with test
%bcond_with libalternatives
%endif
Name:           python-guessit
Version:        4.1.0
Release:        0
Summary:        A library for guessing information from video files
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/wackou/guessit
Source0:        https://files.pythonhosted.org/packages/source/g/guessit/guessit-%{version}.tar.gz
# PATCH-FIX-UPSTREAM remove-six.patch
Patch0:         remove-six.patch
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module babelfish >= 0.6.0}
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module rebulk >= 6}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-babelfish >= 0.6.0
Requires:       python-python-dateutil
Requires:       python-rebulk >= 3.2.0
%if %{?python_version_nodots} < 39
Requires:       python-importlib_resources
%endif
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pytest >= 5}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest-mock >= 3.3.1}
%endif
%python_subpackages

%description
GuessIt is a Python library that extracts as much information as
possible from a video file.
It has a filename matcher that allows to guess a lot of metadata from
a video using its filename only. This matcher works with both movies
and TV shows episodes.

%prep
%autosetup -p1 -n guessit-%{version}
find guessit -type f -name "*.py" -exec sed -i '1{/^#!/d}' {} +

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/guessit
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%pytest
%endif

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative guessit

%post
%python_install_alternative guessit

%postun
%python_uninstall_alternative guessit

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/guessit
%{python_sitelib}/guessit
%{python_sitelib}/guessit-%{version}.dist-info

%changelog
