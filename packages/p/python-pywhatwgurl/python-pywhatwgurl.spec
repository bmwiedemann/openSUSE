#
# spec file for package python-pywhatwgurl
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


# WPT revision the conformance fixtures are pinned to; keep in sync with
# DEFAULT_WPT_COMMIT in the tarball's util/wpt_url_test_data.py on every bump.
%define wpt_commit 181476aa16e8b28a07698bef3a0275fa53dd22e5
%{?sle15_python_module_pythons}
Name:           python-pywhatwgurl
Version:        0.1.2
Release:        0
Summary:        Pure Python implementation of the WHATWG URL Standard
License:        MIT
URL:            https://github.com/pywhatwgurl/pywhatwgurl
Source:         https://files.pythonhosted.org/packages/source/p/pywhatwgurl/pywhatwgurl-%{version}.tar.gz
# The sdist ships the WPT conformance suite but not its fixtures - upstream CI
# downloads them at %%{wpt_commit}. Carry them so %%check is more than 48 unit
# tests. BSD-3-Clause (web-platform-tests), build-time only, never installed.
Source1:        https://raw.githubusercontent.com/web-platform-tests/wpt/%{wpt_commit}/url/resources/urltestdata.json
Source2:        https://raw.githubusercontent.com/web-platform-tests/wpt/%{wpt_commit}/url/resources/setters_tests.json
Source3:        https://raw.githubusercontent.com/web-platform-tests/wpt/%{wpt_commit}/url/resources/percent-encoding.json
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# pythondistdeps does not emit this one (built RPM requires only python(abi)),
# so it has to be declared by hand - rpmlint: python-missing-require idna.
Requires:       python-idna >= 3.4
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module idna >= 3.4}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
pywhatwgurl implements the WHATWG URL Standard in pure Python, providing the
URL and URLSearchParams interfaces with browser-compatible parsing, host and
IDNA handling, percent-encoding and serialisation.

%prep
%autosetup -p1 -n pywhatwgurl-%{version}
mkdir -p tests/conformance/data
cp -a %{SOURCE1} %{SOURCE2} %{SOURCE3} tests/conformance/data/
# Marker upstream's fetch helper writes; the percent-encoding fixture skips
# without it.
cat > tests/conformance/data/wpt_url_test_data_meta.json <<'EOF'
{
  "wpt_base_url": "https://raw.githubusercontent.com/web-platform-tests/wpt/%{wpt_commit}/url/",
  "wpt_commit": "%{wpt_commit}",
  "resources": [
    "percent-encoding.json",
    "setters_tests.json",
    "urltestdata.json"
  ]
}
EOF

%build
%pyproject_wheel

%install
%pyproject_install
# Recompile the installed modules as hash-based bytecode to avoid
# python-bytecode-inconsistent-mtime from the reproducibility-clamped .py mtimes.
%python_expand $python -m compileall -q -f --invalidation-mode=unchecked-hash -o 0 -o 1 -s %{buildroot} %{buildroot}%{$python_sitelib}/pywhatwgurl
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests/conftest.py pushes the source dir onto sys.path[0]; drop the source copy
# so the suite exercises the installed module.
rm -rf pywhatwgurl
# IdnaTestV2/toascii are xfail upstream (tests/conformance/README.md): the idna
# module enforces RFC 5891/5892, stricter than WHATWG's lenient UTS46. Excluded
# here for the same reason - the remaining fixtures are upstream's "in-scope"
# set and must be 100% green. The leading "tests" is not redundant: without a
# positional first argument rpm parses --ignore as a %%pytest macro option.
%pytest tests --ignore=tests/conformance/test_wpt_idna.py --ignore=tests/conformance/test_wpt_toascii.py

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/pywhatwgurl
%{python_sitelib}/pywhatwgurl-%{version}.dist-info

%changelog
