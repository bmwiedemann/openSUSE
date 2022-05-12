#
# spec file for package qpageview
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%define         X_display         ":98"
Name:           python-qpageview
Version:        0.6.2
Release:        0
Summary:        Widget to display page-based documents for Qt5/PyQt5
License:        GPL-3.0-only
URL:            https://github.com/frescobaldi/qpageview
Source:         https://files.pythonhosted.org/packages/source/q/qpageview/qpageview-%{version}.tar.gz
Source1:        qpageview_smoketest.py
# Created with Sphinx by `make latexpdf` in the docs subdir
Source2:        qpageview.pdf
BuildRequires:  %{python_module poppler-qt5}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  xorg-x11-server
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-poppler-qt5
Requires:       python-qt5
BuildArch:      noarch
%python_subpackages

%description
Widget to display page-based documents for Qt5/PyQt5

%prep
%setup -q -n qpageview-%{version}
cp %{SOURCE1} %{SOURCE2} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
#############################################
### Launch a virtual framebuffer X server ###
#############################################
export DISPLAY=%{X_display}
Xvfb %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 2
%python_expand $python qpageview_smoketest.py

%files %{python_files}
%doc ChangeLog README.rst
%license LICENSE
%{python_sitelib}/qpageview
%{python_sitelib}/qpageview-%{version}*-info

%changelog
