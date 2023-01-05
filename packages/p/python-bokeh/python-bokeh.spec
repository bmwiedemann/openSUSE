#
# spec file
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

# too many flaky timeouts on obs servers
%bcond_with testexamples

Name:           python-bokeh%{psuffix}
Version:        3.0.3
Release:        0
Summary:        Statistical interactive HTML plots for Python
License:        BSD-3-Clause
URL:            https://bokeh.org/
# Source-URL:    https://github.com/bokeh/bokeh/
# for the precompiled JS files
Source0:        https://files.pythonhosted.org/packages/source/b/bokeh/bokeh-%{version}.tar.gz
# for the tests
Source1:        https://github.com/bokeh/bokeh/archive/refs/tags/%{version}.tar.gz#/bokeh-%{version}-gh.tar.gz
# Sampledata:   `rm -rf .bokeh && HOME=$PWD bokeh sampledata && tar cJf bokeh-sampledata.tar.xz .bokeh`
Source99:       bokeh-sampledata.tar.xz
BuildRequires:  %{python_module Jinja2 >= 2.9}
BuildRequires:  %{python_module Pillow >= 7.1.0}
BuildRequires:  %{python_module PyYAML >= 3.10}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module contourpy >= 1}
BuildRequires:  %{python_module numpy >= 1.11.3}
BuildRequires:  %{python_module packaging >= 16.8}
BuildRequires:  %{python_module pandas >= 1.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools-git-versioning}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tornado >= 5.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module xyzservices >= 2021.9.1 }
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2 >= 2.9
Requires:       python-Pillow >= 7.1.0
Requires:       python-PyYAML >= 3.10
Requires:       python-base >= 3.8
Requires:       python-contourpy >= 1
Requires:       python-numpy >= 1.11.3
Requires:       python-packaging >= 16.8
Requires:       python-pandas >= 1.2
Requires:       python-tornado >= 5.1
Requires:       python-xyzservices >= 2021.9.1
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module bokeh = %{version}}
BuildRequires:  %{python_module colorcet}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module icalendar}
BuildRequires:  %{python_module json5}
BuildRequires:  %{python_module nbconvert >= 5.4}
BuildRequires:  %{python_module networkx}
BuildRequires:  %{python_module pandas-datareader}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pydot}
BuildRequires:  %{python_module pygraphviz}
BuildRequires:  %{python_module pyshp}
BuildRequires:  %{python_module pytest-asyncio >= 0.18.1}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 1.2.3}
BuildRequires:  %{python_module requests-unixsocket}
BuildRequires:  %{python_module scikit-learn}
BuildRequires:  %{python_module selenium}
BuildRequires:  %{python_module tornado}
BuildRequires:  npm19
%endif
# /SECTION
%python_subpackages

%description
Bokeh is a Python interactive visualization library that targets web
browsers for presentation. It provides concise construction of
graphics in the style of D3.js, and favors delivering this capability
with interactivity over large or streaming datasets.

%prep
%if !%{with test}
%setup -q -n bokeh-%{version}
%else
%setup -q -n bokeh-%{version} -T -b1 -a99
%endif

%if !%{with test}
%build
# Needs the JS files prepackaged in src/bokeh/server/static/, marked by PKG-INFO in sdist
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/bokeh

# Remove hidden files for git repos
%python_expand rm %{buildroot}%{$python_sitelib}/bokeh/server/static/.keep
%endif

%if %{with test}
%check
# npm can't build inside obs without network
deselectname="test_bokehjs or test_ext_commands"
%if %{with testexamples}
# loads external font
deselectname+=" or (test_examples and font-awesome)"
# no squarify
deselectname+=" or (test_examples and treemap)"
%else
# too many flaky timeouts on obs servers
deselectname+=" or test_examples"
%endif
# testfile not available
deselectname+=" or test_with_INLINE_resources"
deselectname+=" or test_with_CDN_resources"
# does not expect pytest-$binsuffix
deselectname+=" or test_detect_current_filename"
# cannot open socket / address already in use / no pattern detected
deselectname+=" or (test_server and test_address)"
deselectname+=" or (test_serve and printed)"
deselectname+=" or test__ioloop_not_forcibly_stopped"
# not json5 serializable
deselectname+=" or test_defaults"
# flaky timeouts
deselectname+=" or (test_deprecation and (test_since or test_message))"
deselectname+=" or (test_document_lifecycle and test_document_on_session_destroyed_exceptions)"
# test can't list modules correctly in test environment
deselectname+=" or (codebase and combined)"
# extraneous fields
deselectname+=" or test_serialization_data_models"
# linting and code structure irrelevant for rpm package
deselectname+=" or test_ruff or test_isort or test_eslint or test_code_quality or test_no_request_host"
# no driver (chromedriver only x86_64)
deselectname+=" or Test_webdriver_control"
# fails when tested with pytest-xdist
deselectname+=" or (TestModelCls and test_get_class)"
deselectname+=" or test_external_js_and_css_resource_ordering"
# for finding the  sampledata (packaged in Source99)
export HOME=$PWD
%pytest -v -m "not selenium" -k "not ($deselectname)" --no-js -n auto
%endif

%post
%python_install_alternative bokeh

%postun
%python_uninstall_alternative bokeh

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc README.md
%python_alternative %{_bindir}/bokeh
%{python_sitelib}/bokeh/
%{python_sitelib}/bokeh-%{version}*-info
%endif

%changelog
