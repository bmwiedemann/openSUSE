#
# spec file for package jlfgr
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


Name:           jlfgr
Summary:        Java look and feel Graphics Repository
License:        SUSE-Redistributable-Content
Group:          Development/Languages/Java
Version:        1.0
Release:        0
Url:            http://java.sun.com/developer/techDocs/hi/repository/
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  fastjar
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
These pages contain a collection of toolbar button graphics. The
graphics have been designed specifically for use with the Java look and
feel. They conform to the Java look and feel Design Guidelines. A set
of attributes accompanies each graphic. This information can easily be
used to create Swing Actions.

As the Human Interface Group, we strive to improve the user experience
for you and your end-users. This graphics repository provides you with
professional quality graphics that will save you development time. Your
end-users benefit by leveraging their knowledge of these graphics and
terminology across different Java look and feel applications.

To provide feedback about the graphics repository, send email to the
Java look and feel Design Team (jlfdesign (at) sun (dot) com).



Authors:
--------
    Java look and feel Design Team (jlfdesign@sun.com)

%prep
%setup -q 

%build
# NOP

%install
install -d -m 755 $RPM_BUILD_ROOT/%{_javadir}
install -m 644 *jar $RPM_BUILD_ROOT/%{_javadir}
(cd $RPM_BUILD_ROOT/%{_javadir}; ln -sf jlfgr-1_0.jar jlfgr-%{version}.jar; ln -sf jlfgr-1_0.jar jlfgr.jar)

%files
%defattr(-,root,root)
%{_javadir}/*.jar

%changelog
