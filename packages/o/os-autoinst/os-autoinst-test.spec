#
# spec file for package os-autoinst%{?name_ext}
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


%define name_ext -test
%define         short_name os-autoinst
Name:           %{short_name}%{?name_ext}
Version:        4.6.1620235366.b165997a
Release:        0
Summary:        test package for os-autoinst
License:        GPL-2.0-or-later
#BuildRequires:  %{short_name} == %{version}
BuildRequires:  %{short_name}

%description
.

%prep
# workaround to prevent post/install failing assuming this file for whatever
# reason
touch %{_sourcedir}/%{short_name}

%build
# call one of the components but not openqa itself which would need a valid
# configuration
isotovideo --help
echo '1;' > main.pm
mkdir needles
cat - > vars.json <<EOF
{
    "CASEDIR": "/tmp"
}
EOF
isotovideo -d casedir=$(pwd -P) productdir=$(pwd -P) |& tee isotovideo.log ||:
grep 'no kvm-img/qemu-img found' isotovideo.log

%install
# disable debug packages in package test to prevent error about missing files
%define debug_package %{nil}

%changelog
