#
# spec file for package colonadjuster
#
# Copyright (c) 2026 Erdinc Daskin <pooperacni@gmail.com>
# License: MIT
#

Name:           colonadjuster
Version:        1.0.0
Release:        0
Summary:        A Fortran code formatter that aligns the double-colon (::) operator
License:        MIT
URL:            https://github.com/CapinolDev/colonadjuster
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  gcc-fortran
BuildRequires:  make

%description
A utility tool written in Fortran that automatically formats and aligns 
the double-colon (::) operator within specified section blocks 
(e.g., using '!#section' and '!#sectionend' markers) to improve code readability.

%prep
%setup -q

%build
%make_build FC=gfortran FFLAGS="%{optflags}"

%install
# Install the binary
install -D -m 0755 colonadjuster %{buildroot}%{_bindir}/colonadjuster

%files
%{_bindir}/colonadjuster
%license LICENSE
%changelog
