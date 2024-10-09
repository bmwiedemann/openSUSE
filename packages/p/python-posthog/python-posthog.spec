#
# spec file for package python-posthog
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
Name:           python-posthog
Version:        3.6.0
Release:        0
Summary:        PostHog is developer-friendly, self-hosted product analytics
License:        MIT
URL:            https://github.com/posthog/posthog-python
Source:         https://files.pythonhosted.org/packages/source/p/posthog/posthog-%{version}.tar.gz
Patch1:         python-posthog-no-mock.patch
Patch2:         python-posthog-no-six.patch
Patch3:         no-more-monotonic.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module backoff >= 1.10.0}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module python-dateutil > 2.1}
BuildRequires:  %{python_module requests >= 2.7}
# /SECTION
BuildRequires:  fdupes
Requires:       python-backoff >= 1.10.0
Requires:       python-python-dateutil > 2.1
Requires:       python-requests >= 2.7
Suggests:       python-black
Suggests:       python-isort
Suggests:       python-flake8
Suggests:       python-flake8-print
Suggests:       python-pre-commit
Suggests:       python-sentry-sdk
Suggests:       python-django
BuildArch:      noarch
%python_subpackages

%description
PostHog is developer-friendly, self-hosted product analytics. Integrate PostHog into any python application

%prep
%autosetup -p1 -n posthog-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# these disabled tests require internet access/valid api key
donttest+=" or test_request or test_upload or test_load_feature_flags_wrong_key or test_excepthook"
%pytest --timeout=40 -k "not (testallexcept ${donttest})" -p no:warnings

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/posthog
%{python_sitelib}/posthog-%{version}.dist-info

%changelog
