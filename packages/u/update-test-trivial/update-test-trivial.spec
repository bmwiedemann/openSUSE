#
# spec file for package update-test-trivial
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           update-test-trivial
Version:        5.1
Release:        0
Summary:        Package for testing the update stack during product development
License:        GPL-2.0+
Group:          System/YaST
Source0:        %{name}.tar.bz2
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Package for testing the update stack during product development.

We will provide a "always" working update for this package so that the
update stack could be easily tested.

%package -n update-test-reboot-needed
Summary:        Test update that requires a system reboot
Group:          System/YaST

%description -n update-test-reboot-needed
Package for testing the update stack during product development.

An update for this package should inform the user that a system
reboot is necessary. This is used, for example, in kernel updates.

%package -n update-test-relogin-suggested
Summary:        Test update that requires a session restart
Group:          System/YaST

%description -n update-test-relogin-suggested
Package for testing the update stack during product development.

An update for this package should inform the user that a session
restart (re-login) is necessary. This is used, for example, in
window manager updates.

%package -n update-test-retracted
Summary:        Test update that should be marked as retracted
Group:          System/YaST

%description -n update-test-retracted
Package for testing the update stack during product development.

An update for this package should mark the update as retracted
in zypper.

%package -n update-test-interactive
Summary:        Test update that requires confirmation
Group:          System/YaST

%description -n update-test-interactive
Package for testing the update stack during product development.

An update for this package should show a message to the user
and wait for confirmation before proceeding. This is used, for
example, in package updates that include proprietary licenses.

%package -n update-test-affects-package-manager
Summary:        Test update that requires a software stack restart
Group:          System/YaST

%description -n update-test-affects-package-manager
Package for testing the update stack during product development.

An update for this package should be installed first by the
update stack and then ask the user to run the update process
again to apply other updates that might be available. This is
used, for example, to update packages from the software update
stack (zypper, libzypp, packagekit, etc).

%package -n update-test-security
Summary:        Test update that includes security fixes
Group:          System/YaST

%description -n update-test-security
Package for testing the update stack during product development.

An update for this package should have its category set to
"security", indicating that one or more security vulnerabilities
are being fixed.

%package -n update-test-feature
Summary:        Test update that includes new features
Group:          System/YaST

%description -n update-test-feature
Package for testing the update stack during product development.

An update for this package should have its category set to
"feature", indicating that it includes a new feature and not
only fixes.

%package -n update-test-optional
Summary:        Test update that is not mandatory
Group:          System/YaST

%description -n update-test-optional
Package for testing the update stack during product development.

An update for this package should have its category set to
"optional". The software stack should not select such updates
for installation by default. This is used, for example, to add
new packages to a product.

%package -n update-test-32bit-pkg
Summary:        Test update that contains a 32bit package
Group:          System/YaST

%description -n update-test-32bit-pkg
Package for testing the update stack during product development.

An update for this package should contain a 32bit-package.

%package -n update-test-broken
Summary:        Test update which should not be installable
Group:          System/YaST

%description -n update-test-broken
Package for testing the update stack during product development.

An update for this package should fail.

%prep
%setup -q -n %{name}

%pre -n update-test-broken
if [ $1 -ne 1 ]; then
    if [ ! -f /.buildenv ]; then
        sed -i -e 's,foo\t,bar\t,g' /some/none/existing/file
    fi
fi

%build
echo "Package: %{name}-%{version}-%{release}" > VERSION
echo -n "Build date: " >> VERSION
LANG=POSIX date -u >> VERSION
for readme in README.update-test*; do
    echo "---" >> $readme
    echo "Package Version : %{version}" >> $readme
    echo "Package Release : %{release}" >> $readme
    echo -n "Generated on    : " >> $readme
    date >> $readme
    echo >> $readme
    echo "  Remember to have a lot of fun!" >> $readme
done

%install

%files
%defattr(-,root,root)
%doc README COPYRIGHT AUTHOR VERSION

%files -n update-test-reboot-needed
%defattr(-,root,root)
%doc README.update-test-reboot-needed

%files -n update-test-interactive
%defattr(-,root,root)
%doc README.update-test-interactive

%files -n update-test-affects-package-manager
%defattr(-,root,root)
%doc README.update-test-affects-package-manager

%files -n update-test-security
%defattr(-,root,root)
%doc README.update-test-security

%files -n update-test-feature
%defattr(-,root,root)
%doc README.update-test-feature

%files -n update-test-optional
%defattr(-,root,root)
%doc README.update-test-optional

%files -n update-test-relogin-suggested
%defattr(-,root,root)
%doc README.update-test-relogin-suggested

%files -n update-test-retracted
%defattr(-,root,root)
%doc README.update-test-retracted

%files -n update-test-32bit-pkg
%defattr(-,root,root)
%doc README.update-test-32bit-pkg

%files -n update-test-broken
%defattr(-,root,root)
%doc README.update-test-broken

%changelog
