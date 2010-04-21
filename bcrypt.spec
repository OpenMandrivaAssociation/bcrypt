Name:		bcrypt
Summary:	A lightweight blowfish file encryption utility
Version:	1.1 
Release:	%mkrel 8 
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}.1.bz2
URL:		http://bcrypt.sourceforge.net/index.html
Group:		Archiving/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	BSD
BuildRequires:	zlib-devel

%description
bcrypt is a blowfish file encryption utility which aims for cross-platform
portability. In addition to providing 448-bit encryption, bcrypt can overwrite
input files with random garbage before deletion in order to make low-level
data recovery much more difficult.

%prep
%setup -q

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
install -m755 bcrypt -D $RPM_BUILD_ROOT%{_bindir}/bcrypt
install -m644 %SOURCE1 -D $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1.bz2

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc README LICENSE
%{_bindir}/*
%{_mandir}/man1/%{name}.1*


