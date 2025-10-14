#
# spec file for package tortoisehg
#
# Copyright (c) 2020 SUSE LLC
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


# only bother with testing on Tumbleweed
%if 0%{?suse_version} >= 1550
%bcond_without test
%else
%bcond_with test
%endif

# python311-nautilus is not available on Leap 15.6, but is required for tortoisehg’s nautilus extension.
%if 0%{?suse_version} > 1600 || 0%{?sle_version} < 150600
%define package_nautilus_extension 1
%else
%define package_nautilus_extension 0
%endif

%if 0%{?suse_version} > 1600
# Tumbleweed
%define pythons python3
%else
%if 0%{?sle_version} >= 150600
%{?sle15_python_module_pythons}
%else
%define pythons                     python3
%endif
%endif

Name:           tortoisehg
Version:        7.0.1
Release:        0
Summary:        Mercurial GUI command line tool
License:        GPL-2.0-only
Group:          Development/Tools/Version Control
URL:            https://tortoisehg.bitbucket.io
Source0:        https://www.mercurial-scm.org/release/%{name}/targz/%{name}-%{version}.tar.gz
Source1:        https://foss.heptapod.net/mercurial/%{name}/thg/-/archive/%{version}/thg-%{version}.tar.gz?path=tests#/thg-%{version}-tests.tar.gz
Source99:       rpmlintrc
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  mercurial
BuildRequires:  mercurial
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module setuptools}
BuildRequires:  update-desktop-files
Requires:       mercurial
Requires:       mercurial
# python311-iniparse is not available in Leap 15.6.
%if 0%{?suse_version} > 1600 || 0%{?sle_version} < 150600
Requires:       %{python_module iniparse >= 0.3.1}
%endif
Recommends:     %{python_module Pygments}
BuildArch:      noarch
BuildRequires:  %{python_module qt5-devel}
Requires:       %{python_module qscintilla-qt5}
Requires:       %{python_module qt5}
%if %{with test}
BuildRequires:  %{python_module Pygments}
# python311-iniparse is not available in Leap 15.6.
%if 0%{?suse_version} > 1600 || 0%{?sle_version} < 150600
BuildRequires:  %{python_module iniparse >= 0.3.1}
%endif
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-qt}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module qscintilla-qt5}
%endif

%description
This package contains the thg command line tool, which provides a graphical
user interface to the Mercurial distributed revision control system.

%if %package_nautilus_extension
%package        nautilus
Summary:        Mercurial GUI plugin to Nautilus file manager
Group:          Development/Tools/Version Control
Requires:       %{name} = %{version}
Requires:       %{python_module nautilus}

%description    nautilus
This package contains the TortoiseHg Gnome/Nautilus extension, which makes the
Mercurial distributed revision control system available in the file manager
with a graphical interface.

Note that the nautilus extension has been deprecated upstream.
%endif

%prep
%autosetup -a1 -p1

%build
%python_build

(cd doc && make html)
rm doc/build/html/.buildinfo

%install
%python_install
%find_lang %{name}
%suse_update_desktop_file -i thg Development RevisionControl
cp %{buildroot}%{_datadir}/pixmaps/%{name}/scalable/apps/thg.svg %{buildroot}/%{_datadir}/pixmaps/thg_logo.svg
rm %{buildroot}%{_datadir}/doc/%{name}/COPYING.txt
%if !%package_nautilus_extension
rm -r %{buildroot}%{_datadir}/nautilus-python
%endif
%fdupes %{buildroot}%{_datadir}
%fdupes doc/build/html
%fdupes %{buildroot}%{python_sitelib}

%check
%if %{with test}
cd thg-%{version}-tests
# needs a custom pytest plugin loader in run-tests.py
export PYTHONPATH="%{buildroot}%{python_sitelib}"
%python_exec tests/run-tests.py -v -m 'not largefiles' tests
%python_exec tests/run-tests.py -v -m largefiles tests
%endif

%files -f %{name}.lang
%license COPYING.txt
%doc doc/build/html/
%{_bindir}/thg
%{_datadir}/applications/thg.desktop
%{_datadir}/pixmaps/%{name}
%{_datadir}/pixmaps/thg_logo.svg
%{python_sitelib}/%{name}
%{python_sitelib}/hgext3rd/
%{python_sitelib}/%{name}-%{version}*-info

%if %package_nautilus_extension
%files nautilus
%license COPYING.txt
%dir %{_datadir}/nautilus-python
%dir %{_datadir}/nautilus-python/extensions
%{_datadir}/nautilus-python/extensions/nautilus-thg.py
%endif

%changelog
