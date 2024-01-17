/*
 * A little helper to wrap around jdupes and create hard/soft links of the
 * dups found. Used in openSUSE rpm.
 *
 * Copyright 2022 Jiri Slaby <jslaby@suse.cz>
 *           2022 Stephan Kulow <coolo@suse.de>
 *
 * SPDX-License-Identifier: MIT
 */

#include <algorithm>
#include <array>
#include <iostream>
#include <list>
#include <map>
#include <string>
#include <sys/param.h>
#include <sys/stat.h>
#include <tuple>
#include <unistd.h>
#include <utility>
#include <vector>

typedef std::map<ino_t, std::vector<std::string>> dups_map;
typedef std::pair<ino_t, size_t> nlink_pair;

bool cmp_nlink(const nlink_pair& a, const nlink_pair& b)
{
    return a.second > b.second;
}

void sort_by_count(const dups_map& in, std::vector<ino_t>& out)
{
    out.clear();
    std::list<nlink_pair> nlinks;
    for (auto it = in.cbegin(); it != in.cend(); ++it) {
        nlinks.push_back(std::make_pair(it->first, it->second.size()));
    }
    nlinks.sort(cmp_nlink);
    for (auto it = nlinks.cbegin(); it != nlinks.cend(); ++it) {
        out.push_back(it->first);
    }
}

void link_file(const std::string& file, const std::string& target, bool symlink)
{
    std::cout << "Linking " << file << " -> " << target << std::endl;
    if (unlink(file.c_str())) {
        std::cerr << "Removing '" << file << "' failed." << std::endl;
        exit(1);
    }
    int ret;
    if (symlink) {
        ret = ::symlink(target.c_str(), file.c_str());
    } else {
        ret = link(target.c_str(), file.c_str());
    }
    if (ret) {
        std::cerr << "Linking '" << file << "' failed." << std::endl;
        exit(1);
    }
}

void handle_dups(const dups_map& dups, const std::string& buildroot, bool symlink)
{
    // all are hardlinks to the same data
    if (dups.size() < 2)
        return;
    std::vector<ino_t> sorted;
    sort_by_count(dups, sorted);
    auto inodes = sorted.begin();
    std::string target = dups.at(*inodes).front();
    if (symlink) {
        target.replace(0, buildroot.length(), "");
    }

    for (++inodes; inodes != sorted.end(); ++inodes) {
        const std::vector<std::string> files = dups.at(*inodes);
        for (auto it = files.begin(); it != files.end(); ++it) {
            link_file(*it, target, symlink);
        }
    }
}

int main(int argc, char** argv)
{
    bool symlink = false;
    std::string root;
    std::string buildroot;
    while (1) {
        int result = getopt(argc, argv, "sb:");
        if (result == -1)
            break; /* end of list */
        switch (result) {
        case 's':
            symlink = true;
            break;
        case 'b':
            buildroot = optarg;
            break;
        default: /* unknown */
            break;
        }
    }
    if (buildroot.empty()) {
        if (symlink) {
            std::cerr << "Missing -b argument to remove bootroot from symlink targets";
            return 1;
        }
        // eliminate final slash from directory argument
        if (buildroot.back() == '/') {
            buildroot.pop_back();
        }
    }
    if (optind < argc) {
        root = argv[optind++];
    } else {
        std::cerr << "Missing directory argument.";
    }
    if (optind < argc) {
        std::cerr << "Too many arguments.";
        return 1;
    }
    /* jdupes options used:
       -q: hide progress indicator
       -p: don't consider files with different owner/group or permission bits as duplicates
       -o name: output order of duplicates
       -r: follow subdirectories
       -H: also report hard links as duplicates
    */
    std::string command = "jdupes -q -p -o name";
    if (!symlink) {
        /* if we create symlinks, avoid looking at hard links being duplicated. This way
           jdupes is faster and won't break them up anyway */
        command += " -H";
    }
    command += " -r '" + root + "'";
    FILE* pipe = popen(command.c_str(), "r");
    if (!pipe) {
        throw std::runtime_error("popen() failed!");
    }
    std::array<char, MAXPATHLEN> buffer;
    dups_map dups;
    while (fgets(buffer.data(), buffer.size(), pipe) != nullptr) {
        std::string line = buffer.data();
        if (line.length() < 2) {
            handle_dups(dups, buildroot, symlink);
            dups.clear();
            continue;
        }
        if (line.back() != '\n') {
            std::cerr << "Too long lines? '" << line << "'" << std::endl;
            return 1;
        }
        line.pop_back();

        struct stat sb;
        if (stat(line.c_str(), &sb)) {
            std::cerr << "Stat on '" << buffer.data() << "' failed" << std::endl;
            return 1;
        }
        dups[sb.st_ino].push_back(line);
    }
    pclose(pipe);

    return 0;
}
