Summary:	Antispam utility
Summary(pl):	Narzêdzie antyspamowe
Name:		mailfilter
Version:	0.5.1
Release:	2
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	de208957b2aaaffe26c0c54c83e2c503
Source1:	%{name}-pl.po
Patch0:		%{name}-pl_po.patch
URL:		http://mailfilter.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ia32	"-fomit-frame-pointer"

%description
Mailfilter is a flexible utility for Unix (-like) operating systems to
get rid of unwanted spam mails, before having to go through the
trouble of downloading them into the local computer. It offers support
for one or many POP3 accounts and is especially useful for dialup
connections via modem, ISDN, etc.
Mailfilter connects to any POP3 mail box and compares part of its
content to a set of user defined filter rules. That way the spam gets
deleted directly on the mail server.
		  
%description -l pl
Mailfilter jest elastycznym narzêdziem dla systemów UNIXopodobnych,
s³u¿±cym do pozbywania siê niechcianego spamu przed pobraniem go na
lokalny komputer z sieci. Obs³uguje wiele kont POP3 i jest nadzwyczaj
u¿yteczny dla po³±czeñ wdzwanianych przez modem, ISDN etc.
Mailfilter ³±czy siê z kontem POP3 i porównuje czê¶ci jego zawarto¶ci
z zestawem regu³ek zdefiniowanych przez u¿ytkownika. W ten sposób spam
zostaje usuniêty bezpo¶rednio na serwerze pocztowym.

%prep
%setup -q
%patch0 -p1
install %{SOURCE1} po/pl.po

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5}}

make install DESTDIR=$RPM_BUILD_ROOT
install man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install man/*.5 $RPM_BUILD_ROOT%{_mandir}/man5
mv -f doc/api/man/man3 $RPM_BUILD_ROOT%{_mandir}
rm -rf doc/api/man

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS NEWS THANKS TODO doc/{api,Doxyfile,FAQ,rcfile.example{1,2},supported_servers}
%lang(it) %doc doc/rcfile.example1.it
%lang(ru) %doc doc/rcfile.example2.ru
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man5/*
