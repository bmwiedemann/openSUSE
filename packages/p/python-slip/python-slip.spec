#
# spec file for package python-slip
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
Name:           python-slip
Version:        0.6.5
Release:        0
Summary:        Miscellaneous convenience, extension and workaround code for Python
License:        GPL-2.0-or-later
Group:          System/Libraries
URL:            https://github.com/nphilipp/python-slip
Source0:        https://github.com/nphilipp/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  %{python_module base}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides the "slip" and the "slip.util" modules.

%package dbus
Summary:        Convenience functions for dbus services
Group:          System/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       python-dbus-python >= 0.80
Requires:       python-decorator
Requires:       python-six
# Don't require any of python-gobject{,2} because slip.dbus works with either one. In
# theory users of slip.dbus should require one or the other anyway to use the
# main loop.
#
# No hard requirement on polkit to allow minimal installs without polkit and
# its dependencies.

%description dbus
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides slip.dbus.service.Object, which is a dbus.service.Object
derivative that ends itself after a certain time without being used and/or if
there are no clients anymore on the message bus, as well as convenience
functions and decorators for integrating a dbus service with PolicyKit.

%ifpython2
%package gtk
Summary:        Code to make auto-wrapping gtk labels
Group:          System/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       python-gtk

%description gtk
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides slip.gtk.set_autowrap(), a convenience function which
lets gtk labels be automatically re-wrapped upon resizing.
%endif

%prep
%setup -q

%build
export PYTHON=python3
make %{?_smp_mflags}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no unit tests found

%files %{python_files}
%license COPYING
%dir %{python_sitelib}/slip/
%dir %{python_sitelib}/slip/_wrappers
%pycache_only %{python_sitelib}/slip/_wrappers/__pycache__
%pycache_only %{python_sitelib}/slip/__pycache__
%{python_sitelib}/slip/__init__.py*
%{python_sitelib}/slip/util
%{python_sitelib}/slip-%{version}-py%{python_version}.egg-info
%{python_sitelib}/slip/_wrappers/__init__.*
%{python_sitelib}/slip/_wrappers/_glib.*

%files %{python_files dbus}
%doc doc/dbus/*
%{python_sitelib}/slip/dbus
%{python_sitelib}/slip.dbus-%{version}-py%{python_version}.egg-info

%ifpython2
%files %{python_files gtk}
%{python_sitelib}/slip/gtk
%{python_sitelib}/slip.gtk-%{version}-py%{python_version}.egg-info
%endif

%changelog
