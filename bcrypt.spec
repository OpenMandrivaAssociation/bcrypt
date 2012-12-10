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




%changelog
* Wed Apr 21 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.1-8mdv2010.1
+ Revision: 537482
- don't define release and version on top of spec.

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 1.1-8mdv2010.0
+ Revision: 424025
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.1-7mdv2008.1
+ Revision: 135828
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Dec 14 2006 Eskild Hustvedt <eskild@mandriva.org> 1.1-7mdv2007.0
+ Revision: 97171
- Yearly rebuild
- Import bcrypt

* Sat Oct 22 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.1-6mdk
- Fix BuildRequires

* Fri May 27 2005 Eskild Hustvedt <eskild@mandriva.org> 1.1-5mdk
- Minor fixes to the manpage (manpage 0.1.1)

* Thu May 26 2005 Eskild Hustvedt <eskild@mandriva.org> 1.1-4mdk
- Fixed the URL (I'll probably stop updating it for today now)

* Thu May 26 2005 Eskild Hustvedt <eskild@mandriva.org> 1.1-3mdk
- Make the spec a tad prettier to pelase Oden :P

* Thu May 26 2005 Eskild Hustvedt <eskild@mandriva.org> 1.1-2mdk
- Source1: Manpage

* Mon May 23 2005 Eskild Hustvedt <eskild@mandriva.org> 1.1-1mdk
- Initial Mandriva Linux package

