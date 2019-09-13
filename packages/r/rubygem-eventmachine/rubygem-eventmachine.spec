#
# spec file for package rubygem-eventmachine
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-eventmachine
Version:        1.2.7
Release:        0
%define mod_name eventmachine
%define mod_full_name %{mod_name}-%{version}
# MANUAL
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  pkg-config
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubydevel}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  ruby-macros >= 5
Url:            http://rubyeventmachine.com
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-eventmachine-rpmlintrc
Source2:        gem2rpm.yml
Summary:        Ruby/EventMachine library
License:        Ruby OR GPL-2.0-only
Group:          Development/Languages/Ruby

%description
EventMachine implements a fast, single-threaded engine for arbitrary network
communications. It's extremely easy to use in Ruby. EventMachine wraps all
interactions with IP sockets, allowing programs to concentrate on the
implementation of network protocols. It can be used to create both network
servers and clients. To create a server or client, a Ruby program only needs
to specify the IP address and port, and provide a Module that implements the
communications protocol. Implementations of several standard network protocols
are provided with the package, primarily to serve as examples. The real goal
of EventMachine is to enable programs to easily interface with other programs
using TCP/IP, especially if custom protocols are required.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGELOG.md LICENSE README.md" \
  -f
%gem_cleanup

%gem_packages

%changelog
