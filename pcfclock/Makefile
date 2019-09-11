obj-m		:= pcfclock.o

# Where to install the modules
MOD_DIR := misc

.PHONY: modules install clean modules_add

install : modules_add
modules modules_add clean:
	$(MAKE) -C $(KERNEL_SOURCE) $@ SUBDIRS=$(CURDIR)
