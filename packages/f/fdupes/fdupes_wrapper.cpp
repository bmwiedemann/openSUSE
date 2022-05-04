/*
 * A little helper to wrap around fdupes and create hard/soft links of the
 * dups found. Used in openSUSE rpm.
 *
 * Copyright 2022 Jiri Slaby <jslaby@suse.cz>
 *           2022 Stephan Kulow <coolo@suse.de>
 *           2022 Stefan Brüns <stefan.bruens@rwth-aachen.de>
 *
 * SPDX-License-Identifier: MIT
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <sys/param.h>
#include <sys/stat.h>
#include <unistd.h>
#include <utility>
#include <vector>
#include <sstream>

using namespace std;

struct file_entry
{
    ino_t inode;
    nlink_t link_count;
    string path;

    file_entry(ino_t i, nlink_t n, string&& p)
    : inode(i), link_count(n), path(move(p)) {}
};
using dup_set = vector<file_entry>;

enum class Operation {
    Symlink,
    Hardlink,
    DryRun,
};

vector<string> split_paths(const string& path)
{
    string token;
    vector<string> paths;
    stringstream ss(path);
    while (getline(ss, token, '/')) {
        if (token == "..") {
            paths.pop_back();
        } else if (token != "." || ss.eof()) {
            paths.push_back(token);
        }
    }
    return paths;
}

string merge_paths(const vector<string>& paths)
{
    string path;
    for (const auto& s : paths) {
        if (s.empty())
            continue;
        if (!path.empty())
            path += "/";
        path += s;
    }

    return path;
}

string relative(const string& p1, const string& p2)
{
    vector<string> paths1 = split_paths(p1);
    paths1.pop_back();
    vector<string> paths2 = split_paths(p2);
    vector<string> paths;
    vector<string>::const_iterator it1 = paths1.begin();
    vector<string>::const_iterator it2 = paths2.begin();
    // first remove the common parts
    while (it1 != paths1.end() && *it1 == *it2) {
        it1++;
        it2++;
    }
    for (; it1 != paths1.end(); ++it1) {
        paths.push_back("..");
    }
    for (; it2 != paths2.end(); ++it2) {
        paths.push_back(*it2);
    }

    return merge_paths(paths);
}

void link_file(const std::string& file, const std::string& target, Operation op)
{
    std::cout << "Linking " << file << " -> " << target << std::endl;
    if (op == Operation::DryRun)
        return;

    if (unlink(file.c_str())) {
        std::cerr << "Removing '" << file << "' failed." << std::endl;
        exit(1);
    }
    int ret;
    if (op == Operation::Symlink) {
        ret = ::symlink(target.c_str(), file.c_str());
    } else {
        ret = link(target.c_str(), file.c_str());
    }
    if (ret) {
        std::cerr << "Linking '" << file << "' failed." << std::endl;
        exit(1);
    }
}

std::string target_for_link(string target, const std::string &file, Operation op)
{
    if (op == Operation::Hardlink) // hardlinks don't care
        return target;

    return relative(file, target);
}

void handle_dups(dup_set& dups, Operation op)
{
    // calculate number of hardlinked duplicates found, for each file
    // this may be different than the st_nlink value
    std::sort(dups.begin(), dups.end(), [](const file_entry& a, const file_entry& b) {
        return a.inode < b.inode;
    });
    auto first = dups.begin();
    while (first != dups.end()) {
        auto r = equal_range(first, dups.end(), *first, [](const file_entry& a, const file_entry& b) {
            return a.inode < b.inode;
        });
        for (auto i = r.first; i != r.second; ++i) {
            i->link_count = std::distance(r.first, r.second);
        }
        first = r.second;
    }

    // use the file with most hardlinks as target
    // in case of ties, sort by name to get a stable order for reproducible builds
    std::sort(dups.begin(), dups.end(), [](const file_entry& a, const file_entry& b) {
        if (a.link_count == b.link_count)
            return a.path > b.path;
        return a.link_count > b.link_count;
    });

    const string& target = dups[0].path;

    for (const file_entry& e : dups) {
        // skip duplicates hardlinked to first entry
        if (e.inode == dups[0].inode)
            continue;

        link_file(e.path, target_for_link(target, e.path, op), op);
    }
}

int main(int argc, char** argv)
{
    Operation op = Operation::Hardlink;
    std::vector<std::string> roots;
    while (1) {
        int result = getopt(argc, argv, "sn");
        if (result == -1)
            break; /* end of list */
        switch (result) {
        case 's':
            op = Operation::Symlink;
            break;
        case 'n':
            op = Operation::DryRun;
            break;
        default: /* unknown */
            break;
        }
    }
    while (optind < argc) {
        std::string root = argv[optind++];
        if (root.front() != '/') {
            char buffer[PATH_MAX];
            root = std::string(getcwd(buffer, PATH_MAX)) + '/' + root;
        }
        roots.push_back(root);
    }

    if (roots.empty()) {
        std::cerr << "Missing directory argument.";
        return 1;
    }
    /* fdupes options used:
       -q: hide progress indicator
       -p: don't consider files with different owner/group or permission bits as duplicates
       -n: exclude zero-length files from consideration
       -r: follow subdirectories
       -H: also report hard links as duplicates
    */
    std::string command = "fdupes -q -p -r -n";
    if (op != Operation::Symlink) {
        /* if we create symlinks, avoid looking at hard links being duplicated. This way
           fdupes is faster and won't break them up anyway */
        command += " -H";
    }
    for (auto it = roots.begin(); it != roots.end(); ++it) {
        command += " '" + *it + "'";
    }
    FILE* pipe = popen(command.c_str(), "r");
    if (!pipe) {
        throw std::runtime_error("popen() failed!");
    }
    std::vector<char> buffer;
    buffer.resize(MAXPATHLEN);

    dup_set dups;
    while (fgets(buffer.data(), buffer.size(), pipe) != nullptr) {
        std::string line = buffer.data();
        if (line.length() < 2) {
            handle_dups(dups, op);
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
        dups.emplace_back(sb.st_ino, 0, std::move(line));
    }
    pclose(pipe);

    return 0;
}
