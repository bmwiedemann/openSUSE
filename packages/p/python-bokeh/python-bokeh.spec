#
# spec file for package python-bokeh
#
# Copyright (c) 2021 SUSE LLC
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


%define skip_python2 1
%define skip_python36 1
%bcond_without  tests
Name:           python-bokeh
Version:        2.4.0
Release:        0
Summary:        Statistical interactive HTML plots for Python
License:        BSD-3-Clause
URL:            https://github.com/bokeh/bokeh/
Source0:        https://files.pythonhosted.org/packages/source/b/bokeh/bokeh-%{version}.tar.gz
Source1:        https://github.com/bokeh/bokeh/raw/%{version}/conftest.py
BuildRequires:  %{python_module Jinja2 >= 2.9}
BuildRequires:  %{python_module Pillow >= 7.1.0}
BuildRequires:  %{python_module PyYAML >= 3.10}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module numpy >= 1.11.3}
BuildRequires:  %{python_module packaging >= 16.8}
BuildRequires:  %{python_module python-dateutil >= 2.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tornado >= 5.1}
BuildRequires:  %{python_module typing_extensions >= 3.7.4}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildConflicts: python-buildservice-tweak
Requires:       python-Jinja2 >= 2.9
Requires:       python-Pillow >= 7.1.0
Requires:       python-PyYAML >= 3.10
Requires:       python-numpy >= 1.11.3
Requires:       python-packaging >= 16.8
Requires:       python-python-dateutil >= 2.1
Requires:       python-tornado >= 5.1
Requires:       python-typing_extensions >= 3.7.4
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     python-python-dateutil
BuildArch:      noarch
# SECTION test requirements
%if %{with tests}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module nbconvert}
BuildRequires:  %{python_module networkx}
BuildRequires:  %{python_module pydot}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module selenium}
BuildRequires:  nodejs >= 14
%endif
# /SECTION
%python_subpackages

%description
Bokeh is a Python interactive visualization library that targets web
browsers for presentation. It provides concise construction of
graphics in the style of D3.js, and favors delivering this capability
with interactivity over large or streaming datasets.

%prep
%autosetup -p1 -n bokeh-%{version}
# add conftest.py for pytest fixtures
cp %{SOURCE1} .
# remove external mock in favor of unittest.mock
find tests -name '*.py' -exec \
  sed -i {} \
  -e 's/^import mock/from unittest import mock/' \
  -e 's/^from mock import mock/from unittest import mock/' \
  -e 's/^from mock import/from unittest.mock import/' \
  ';'

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/bokeh

# Remove hidden files
%python_expand rm %{buildroot}%{$python_sitelib}/bokeh/server/static/.keep

# Remove test and script files
%python_expand rm -rf %{buildroot}%{$python_sitelib}/scripts/
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests/

%if %{with tests}
%check
# GUI based selenium with chromedriver setup within OBS is hard/impossible
deselectmarker="selenium"
# sampledata: no download
deselectmarker+=" or sampledata"
# npm can't build inside obs without network
deselectname="test_ext_commands"
# testfile not packaged in sdist
deselectname+=" or test_with_INLINE_resources"
deselectname+=" or test_with_CDN_resources"
# does not expect pytest-$binsuffix
deselectname+=" or test_detect_current_filename"
# no browser installed
deselectname+=" or test_webdriver"
%pytest -m "not ($deselectmarker)" -k "not ($deselectname)"
%endif

%post
%python_install_alternative bokeh

%postun
%python_uninstall_alternative bokeh

%files %{python_files}
%license LICENSE.txt
%doc CHANGELOG README.md
%python_alternative %{_bindir}/bokeh
%{python_sitelib}/bokeh/
%{python_sitelib}/bokeh-%{version}-py%{python_version}.egg-info

%changelog
