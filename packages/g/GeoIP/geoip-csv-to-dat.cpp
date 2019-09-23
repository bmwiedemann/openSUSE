/* geoip-csv-to-dat - convert a country database from CSV to GeoIP binary format
 *
 * Copyright (c) 2009 Kalle Olavi Niemitalo.
 * Copyright (c) 2011 Patrick Matthäi
 * Copyright (c) 2014 Andrew Moise
 *
 * Permission to use, copy, modify, and/or distribute this software for any
 * purpose with or without fee is hereby granted, provided that the above
 * copyright notice and this permission notice appear in all copies.
 *
 * THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
 * WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
 * ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
 * WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
 * ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
 * OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
 */

#define _GNU_SOURCE 1
#include <algorithm>
#include <arpa/inet.h>
#include <cerrno>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <error.h>
#include <fstream>
#include <getopt.h>
#include <iostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <sys/socket.h>
#include <sys/types.h>
#include <sysexits.h>
#include <vector>
#include <GeoIP.h>

// Format of GeoIP Database files
// ======================================
//
// 1. Binary trie mapping IP addresses to locations.
// 2. Information about each location (only in city DBs).
// 3. Optional unused data.
// 4. Optional database-info block.
// 5. Optional structure-info block.
//
// Binary trie
// -----------
//
// The trie treats IP addresses as bit sequences and maps them to
// location numbers.
//
// In the country database format, each such number is a country ID
// that GeoIP_id_by_ipnum() would return.  The meanings of country IDs
// are hardcoded in libGeoIP and cannot be overridden by the database.
//
// In the city database format, each such number is a position to seek
// to, within section #2 (information about each location), in order
// to find a record giving information about the location associated
// with that IP.
//
// The root node of the trie is at the beginning of the file, and the
// other nodes then follow it.	Each node has the same size and
// consists of two little-endian pointers that correspond to the two
// possible values of a bit.  The pointers are 24-bit, and each node
// is thus 6 bytes long.
//
// To traverse the trie, you go one bit at a time through the IP
// address you're looking up -- starting at bit 0, and starting at the
// root node of the trie. For each bit, you look at the current node,
// and take the left branch (the first of the two pointers) if the bit
// is 0, otherwise take the right branch. It is allowed for a node
// pointer to refer back to earlier nodes in the file, but loops are
// not allowed.
//
// If the pointer you're looking at is less than the total number of
// nodes in the trie, it indicates the next node you should
// examine. If the pointer you're looking at is greater than or equal
// to the total number of nodes, it indicates a leaf -- the end of
// your search.
//
// The meaning of the leaf pointers depends on the database type:
//
// In country databases, 0xFFFF?? indicates that the country ID
// for that IP address is equal to the ?? part. 0xFFFF00 indicates
// that the IP address you queried is not in the database.
//
// City databases contain an extra segment which contains location
// information records. A leaf pointer equal to (number of nodes in
// the trie + X) indicates that the location information for the IP
// address you queried can be found in the location information
// segment, at offset X. A leaf pointer exactly equal to the number of
// nodes in the trie indicates that the location information for the
// IP address you queried is not stored in this database.
//
// Location segment
// --------------------
//
// City databases contain a location segment. Each record in this
// segment contains information about a single location which IP
// addresses may be mapped to. Pointers to records in this segment are
// contained within leaf nodes of the trie; each record contains, in
// this order:
//
// * A country ID, as a single byte
// * A "region" (generally state or province), as a NULL-terminated string
// * A city name, as a NULL-terminated string
// * A postal code, as a NULL-terminated string
// * Encoded latitude, as a little-endian 3-byte integer. To convert
//   back to actual latitude, divide by 10000 and subtract 180.
// * Encoded longitude, as a little-endian 3-byte integer. To convert
//   back to actual longitude, divide by 10000 and subtract 180.
// * Area code and metro code (ONLY if the country is US). These are
//   encoded into a single little-endian 3-byte integer. The area code
//   is the encoded value modulo 1000, and the metro code is the
//   encoded value divided by 1000. If the country is not US, this
//   field is not present.
//
// The string fields may be equal to empty strings, but all fields are
// always included (except area/metro code, which is included if and
// only if the country is US).
//
// All strings seem to be in ISO-8859-1 encoding.
//
// Optional unused data
// --------------------
//
// The file format permits any amount of extra data between the binary
// trie and the optional blocks.
//
// Optional database-info block
// ----------------------------
//
// Near the end of the file, there may be a three-byte tag (0x00 0x00
// 0x00) followed by at most DATABASE_INFO_MAX_SIZE - 1 = 99 bytes of
// text that describes the database.  GeoIP_database_info() returns
// this text and appends a terminating '\0'.
//
// The GeoLite Country IPv4 database downloadable from MaxMind
// includes this database-info block.
//
// Optional structure-info block
// -----------------------------
//
// At the very end of the file, there may be a three-byte tag (0xFF
// 0xFF 0xFF) followed by at most STRUCTURE_INFO_MAX_SIZE - 1 = 19
// bytes.  The first byte is the database type,
// e.g. GEOIP_COUNTRY_EDITION = 1 or GEOIP_COUNTRY_EDITION_V6 = 12,
// possibly with 105 added to it.  Type-specific information then
// follows.  There is no type-specific information for the country
// editions.
//
// The GeoLite Country IPv4 database downloadable from MaxMind does
// not include this structure-info block.



/*************************************************
 * Binary trie
 *
 * This section implements a data structure representing the trie
 * which, within a .dat file, maps IP address ranges to locations.
 *************************************************/

namespace {
	class binary_trie
	{
	public:
		typedef uint_fast32_t edge_type;
		struct node
		{
			edge_type edges[2];
		};

		explicit binary_trie(edge_type leaf);
		void set_range(
			const uint8_t range_min[],
			const uint8_t range_max[],
			std::size_t bit_count,
			edge_type leaf);
		void reorder_depth_first();
		void reorder_in_blocks(std::size_t bytes_per_block);

		std::vector<node>::iterator nodes_begin() { return nodes.begin(); }
		std::vector<node>::iterator nodes_end() { return nodes.end(); }

	private:
		std::vector<node> nodes;

		// This could be std::vector<bool> but that seems slower.
		typedef std::vector<uint8_t> bits_vector;

		void set_range_in_node(
			const bits_vector *min_bits,
			const bits_vector *max_bits,
			std::size_t bit_pos,
			edge_type edit_node,
			edge_type leaf);
		void set_range_in_edge(
			const bits_vector *min_bits,
			const bits_vector *max_bits,
			std::size_t bit_pos,
			edge_type edit_node,
			bool bit,
			edge_type leaf);
		void reorder(
			const std::vector<edge_type> &old_to_new,
			const std::vector<edge_type> &new_to_old);
	};
}

/** Construct a binary trie and its root node.
 *
 * \param leaf
 * Both edges of the root node will initially point to this leaf.
 * The caller should provide a value that means nothing was found.  */
binary_trie::binary_trie(edge_type leaf)
{
	const node node = {{ leaf, leaf }};
	nodes.push_back(node);
}

/** Edit the trie so it maps a range of bit sequences to the same
 * leaf.
 *
 * \param range_min
 * The first bit sequence in the range.  Eight bits are packed in each
 * byte.  The most significant bit of the whole sequence is in the
 * most significant bit of the first byte.
 *
 * \param range_max
 * The last bit sequence in the range.
 *
 * \param bit_count
 * The number of bits in both sequences.
 *
 * \param leaf
 * The leaf to which all the bit sequences in the range should be
 * mapped.  */
void
binary_trie::set_range(
	const uint8_t range_min[],
	const uint8_t range_max[],
	std::size_t bit_count,
	edge_type leaf)
{
	bits_vector min_bits(bit_count);
	bits_vector max_bits(bit_count);
	for (std::size_t i = 0; i < bit_count; ++i) {
		std::size_t byte_pos = i / 8;
		uint8_t mask = 1 << ((~i) % 8);
		min_bits[i] = ((range_min[byte_pos] & mask) != 0);
		max_bits[i] = ((range_max[byte_pos] & mask) != 0);
	}
	set_range_in_node(&min_bits, &max_bits, 0, 0, leaf);
}

/** Edit a node in the trie so it maps a range of bit sequences to the
 * same leaf.
 *
 * \param min_bits
 * The first bit sequence in the range, or NULL if unbounded.
 *
 * \param max_bits
 * The last bit sequence in the range, or NULL if unbounded.
 *
 * \param bit_pos
 * Which bit in the sequences corresponds to \a edit_node.
 *
 * \param edit_node
 * The node to be modified.
 *
 * \param leaf
 * The leaf to which all the bit sequences in the range should be
 * mapped.  */
void
binary_trie::set_range_in_node(
	const bits_vector *min_bits,
	const bits_vector *max_bits,
	std::size_t bit_pos,
	edge_type edit_node,
	edge_type leaf)
{
	if (!min_bits || (*min_bits)[bit_pos] == false) {
		set_range_in_edge(min_bits,
				  (max_bits && (*max_bits)[bit_pos] == false)
				  ? max_bits : NULL,
				  bit_pos + 1, edit_node, false, leaf);
	}
	if (!max_bits || (*max_bits)[bit_pos] == true) {
		set_range_in_edge((min_bits && (*min_bits)[bit_pos] == true)
				  ? min_bits : NULL,
				  max_bits,
				  bit_pos + 1, edit_node, true, leaf);
	}
}

/** Edit an edge in the trie so it maps a range of bit sequences to
 * the same leaf.
 *
 * \param min_bits
 * The first bit sequence in the range, or NULL if unbounded.
 *
 * \param max_bits
 * The last bit sequence in the range, or NULL if unbounded.
 *
 * \param bit_pos
 * Which bit in the sequences corresponds to \a bit.
 *
 * \param edit_node
 * The node in which the edge to be modified is located.
 *
 * \param bit
 * Which edge of \a edit_node should be modified.
 *
 * \param leaf
 * The leaf to which all the bit sequences in the range should be
 * mapped.  */
void
binary_trie::set_range_in_edge(
	const bits_vector *min_bits,
	const bits_vector *max_bits,
	std::size_t bit_pos,
	edge_type edit_node,
	bool bit,
	edge_type leaf)
{
	// Check if the range fills this edge entirely.
	bool entire = true;
	if (min_bits
	    && std::find(min_bits->begin() + bit_pos, min_bits->end(),
			 true) != min_bits->end())
		entire = false;
	if (max_bits
	    && std::find(max_bits->begin() + bit_pos, max_bits->end(),
			 false) != max_bits->end())
		entire = false;

	if (entire) {
		nodes[edit_node].edges[bit] = leaf;
	} else {
		edge_type next = nodes[edit_node].edges[bit];
		if (next >= nodes.size()) {
			const node new_node = {{ next, next }};
			next = nodes.size();
			nodes.push_back(new_node);
			nodes[edit_node].edges[bit] = next;
		}

		set_range_in_node(min_bits, max_bits, bit_pos,
				  next, leaf);
	}
}

/** Renumber the nodes in depth-first order.  */
void
binary_trie::reorder_depth_first()
{
	std::vector<edge_type> old_to_new, new_to_old;
	std::stack<edge_type> depth_first;
	old_to_new.resize(nodes.size(), -1);
	new_to_old.reserve(nodes.size());
	depth_first.push(0);
	while (!depth_first.empty()) {
		const edge_type edge = depth_first.top();
		depth_first.pop();
		if (edge < nodes.size()) {
			old_to_new[edge] = new_to_old.size();
			new_to_old.push_back(edge);
			depth_first.push(nodes[edge].edges[1]);
			depth_first.push(nodes[edge].edges[0]);
		}
	}
	reorder(old_to_new, new_to_old);
}

/** Renumber the nodes to make lookups use CPU and disk caches more
 * effectively.
 *
 * First group the nodes into blocks so that each block contains the
 * root of a subtrie and as many levels of its descendants as will
 * fit.  This way, after the root is paged in, the next few lookup
 * steps need not page in anything else.  Then, sort the nodes of each
 * block in depth-first order.  That should give each lookup almost
 * 1/2 chance to find the next node immediately adjacent.
 *
 * With a block size of 1024 bytes, this renumbering reduces the time
 * required for random lookups by about 1.1%, compared to a plain
 * depth-first order.  However, it's still 2.3% slower than the
 * database optimized by MaxMind.  */
void
binary_trie::reorder_in_blocks(
	std::size_t bytes_per_block)
{
	const edge_type none = -1;
	std::vector<edge_type> old_to_new, new_to_old;
	ssize_t bytes_left = bytes_per_block;
	old_to_new.resize(nodes.size(), none);
	new_to_old.reserve(nodes.size());
	for (edge_type subtrie = 0; subtrie < nodes.size(); ++subtrie) {
		// If subtrie has already been added to the output,
		// ignore it.
		if (old_to_new[subtrie] != none)
			continue;

		// Walk breadth-first from subtrie until we have a
		// block full of nodes or the subtrie runs out.  Don't
		// add these nodes immediately to the output, however.
		// Instead just list them in nodes_in_block.
		std::set<edge_type> nodes_in_block;
		std::queue<edge_type> breadth_first;
		breadth_first.push(subtrie);
		if (bytes_left <= 0)
			bytes_left += bytes_per_block;
		while (bytes_left > 0 && !breadth_first.empty()) {
			edge_type edge = breadth_first.front();
			breadth_first.pop();
			if (edge >= nodes.size())
				continue;

			// Let the last node of the block straddle the
			// block boundary.  That's better than making
			// the hotter first node do so.
			bytes_left -= 6;
			nodes_in_block.insert(edge);

			breadth_first.push(nodes[edge].edges[0]);
			breadth_first.push(nodes[edge].edges[1]);
		}

		// Add the nodes from nodes_in_block to the output in
		// depth-first order.  This assumes they are all
		// reachable from subtrie.
		std::stack<edge_type> depth_first;
		depth_first.push(subtrie);
		while (!depth_first.empty()) {
			edge_type edge = depth_first.top();
			depth_first.pop();
			if (nodes_in_block.find(edge)
			    == nodes_in_block.end())
				continue;

			old_to_new[edge] = new_to_old.size();
			new_to_old.push_back(edge);

			depth_first.push(nodes[edge].edges[1]);
			depth_first.push(nodes[edge].edges[0]);
		}
	}
	reorder(old_to_new, new_to_old);
}

void
binary_trie::reorder(
	const std::vector<edge_type> &old_to_new,
	const std::vector<edge_type> &new_to_old)
{
	std::vector<node> new_nodes;
	new_nodes.reserve(new_to_old.size());
	for (std::vector<edge_type>::const_iterator
		     it = new_to_old.begin();
	     it != new_to_old.end(); ++it) {
		node new_node;
		for (int bit = 0; bit <= 1; ++bit) {
			edge_type old_edge = nodes[*it].edges[bit];
			if (old_edge < nodes.size())
				new_node.edges[bit] = old_to_new[old_edge];
			else
				new_node.edges[bit] = old_edge;
		}
		new_nodes.push_back(new_node);
	}
	swap(new_nodes, nodes);
}

/*************************************************
 * CSV file support
 *
 * This section implements reading from .csv files.
 *************************************************/

namespace {
	/** Interface for classes interested in .csv data -- this should be
	 * implemented and then passed to csv_read_file(), which will then
	 * call read_csv_line(), providing the data in the .csv file. */
	class csv_data_reader
	{
	public:
		virtual ~csv_data_reader() {}

		virtual void read_csv_line(const char *csv_file_name,
					   int csv_line_number,
					   std::vector<std::string> &fields) = 0;
	};
}

namespace {
	/** Convert a line from a .csv file into a vector of
	 *  tokens. For internal use by the .csv reading code. */
	void
	csv_line_to_vector(
		const std::string &line,
		std::vector<std::string> &fields)
	{
		fields.clear();
		std::vector<char> field;
		bool quoted = false;
		bool spaces_after_comma = false;
		for (std::string::const_iterator it = line.begin();
		     it != line.end(); ++it) {
			if (*it == '"') {
				quoted = !quoted;
				spaces_after_comma = false;
			} else if (*it == ',' && !quoted) {
				fields.push_back(std::string(field.begin(), field.end()));
				field.clear();
				spaces_after_comma = true;
			} else if (*it == ' ' && spaces_after_comma) {
			} else {
				field.push_back(*it);
				spaces_after_comma = false;
			}
		}
		fields.push_back(std::string(field.begin(), field.end()));
	}

	/** Load data from a CSV-formatted stream.
	 *
	 * \param reader
	 * The reader to call for each line of the CSV
	 *
	 * \param csv_file_name
	 * The name of the file that \a csv_stream is reading.
	 * This string is used only for error messages.
	 *
	 * \param csv_stream
	 * The stream to read from.   */
	void
	csv_read_stream(
		csv_data_reader &reader,
		const char *csv_file_name,
		std::istream &csv_stream)
	{
		std::string csv_line;
		std::vector<std::string> csv_fields;
		int csv_line_number = 0;
		while (getline(csv_stream, csv_line)) {
			++csv_line_number;
			csv_line_to_vector(csv_line, csv_fields);
			reader.read_csv_line(csv_file_name, csv_line_number, csv_fields);
		}
		if (csv_stream.bad()) {
			error(EX_IOERR, errno, "%s", csv_file_name);
		}
	}

	/** Load data from a CSV-formatted file or standard input.
	 *
	 * \param reader
	 * The reader to call for each line of the CSV.
	 *
	 * \param csv_file_name
	 * The name of the CSV file that should be read, or "-" for
	 * standard input.   */
	void
	csv_read_file(
		csv_data_reader &reader,
		const char *csv_file_name)
	{
		if (std::strcmp(csv_file_name, "-") == 0) {
			csv_read_stream(reader, csv_file_name, std::cin);
		} else {
			std::ifstream csv_stream(csv_file_name, std::ios::in);
			if (!csv_stream) {
				error(EX_NOINPUT, errno, "%s", csv_file_name);
			}
			csv_read_stream(reader, csv_file_name, csv_stream);
		}
	}
}

/*************************************************
 * .dat file support
 *
 * This section implements support code for writing out .dat files in
 * Maxmind DB format.
 *************************************************/

namespace {

	/** .dat file writer class
	 *
	 * To write out a .dat file, construct a dat_writer, then call
	 * (in this order):
	 *
	 * write_trie()
	 * write_database_info (optional)
	 * write_structure_info()
	 *
	 * Setting dat_file_name to "-" will write to standard output;
	 * otherwise, a file will be created, and closed when the
	 * dat_writer is deleted. */

	class dat_writer
	{
	public:
		dat_writer(const char *dat_file_name, GeoIPDBTypes database_type);
		virtual ~dat_writer();

		void write_trie(binary_trie &trie);
		void write_database_info(const char *database_info);
		virtual void write_structure_info();

	protected:
		std::ostream *dat_stream;
		bool need_to_delete_stream;
		std::string dat_file_name;
		GeoIPDBTypes database_type;
	};

}

dat_writer::dat_writer(const char *dat_file_name, GeoIPDBTypes database_type):
	dat_file_name(dat_file_name),
	database_type(database_type)
{
	if (std::strcmp(dat_file_name, "-") == 0) {
		dat_stream = &std::cout;
		need_to_delete_stream = false;
	} else {
		dat_stream = new std::ofstream(dat_file_name, std::ios::out | std::ios::binary);
		if (!dat_stream) {
			error(EX_CANTCREAT, errno, "%s", dat_file_name);
		}
		need_to_delete_stream = true;
	}
}

dat_writer::~dat_writer()
{
	if (need_to_delete_stream)
		delete dat_stream;
}

void dat_writer::write_trie(binary_trie &trie)
{
	for (std::vector<binary_trie::node>::iterator it = trie.nodes_begin();
	     it != trie.nodes_end(); ++it)
	{
		union {
			uint8_t bytes[6];
			char chars[6];
		} binary = {{
			(uint8_t) ((it->edges[0]      ) & 0xFF),
			(uint8_t) ((it->edges[0] >>  8) & 0xFF),
			(uint8_t) ((it->edges[0] >> 16) & 0xFF),
			(uint8_t) ((it->edges[1]      ) & 0xFF),
			(uint8_t) ((it->edges[1] >>  8) & 0xFF),
			(uint8_t) ((it->edges[1] >> 16) & 0xFF)
		}};
		dat_stream->write(binary.chars, 6);
		if (dat_stream->bad())
			error(EX_IOERR, errno, "%s", dat_file_name.c_str());
	}
}

void dat_writer::write_database_info(const char *database_info)
{
	const char tag[3] = { 0, 0, 0 };
	dat_stream->write(tag, 3);
	dat_stream->write(database_info, std::strlen(database_info));
	if (dat_stream->bad()) {
		error(EX_IOERR, errno, "%s", dat_file_name.c_str());
	}
}

void dat_writer::write_structure_info()
{
	const char structure_info[4] = { (char)0xFF, (char)0xFF, (char)0xFF,
					 (char)database_type };
	dat_stream->write(structure_info, 4);
}

/*************************************************
 * .dat file writer class, extended for city DBs
 *************************************************/

namespace
{

	class city_dat_writer : public dat_writer
	{
	public:
		// All serialized location information, in one big
		// undifferentiated block
		std::stringstream location_stream;

		// Seek offset of each location within
		// location_stream (relative to the beginning of
		// location_stream). An offset of -1 means that that
		// location is not in the table (can happen if the
		// location info's out of order).
		std::vector<int> location_pos;

		// Set of location IDs that are actually going to be used;
		// we'll silently ignore any locations not in this set.
		std::set<int> needed_locations;
	  
		city_dat_writer(const char *dat_file_name, GeoIPDBTypes database_type);

		// Notify of a location ID we need -- this MUST be
		// called for every location ID you care about before
		// the location CSV is read; any ID not explicitly
		// notified will be discarded.
		void notify_need_location(int loc_id);
		
		void serialize_location_info(std::vector<std::string> &info,
					     const char *input_file_name,
					     int input_line_number);

		void finalize_location_offsets(binary_trie &trie);
		void write_locations();
		virtual void write_structure_info(binary_trie &trie);
	};

}

city_dat_writer::city_dat_writer(const char *dat_file_name, GeoIPDBTypes database_type)
	: dat_writer(dat_file_name, database_type)
{ }

void city_dat_writer::notify_need_location(int loc_id)
{
	needed_locations.insert(loc_id);
}

void city_dat_writer::finalize_location_offsets(binary_trie &trie)
{
	// We're going to convert the location numbers in the trie
	// into the final location numbers we're going to want to
	// write to disk. Previous to this call, leaf nodes in the
	// trie have the value:
	//
	// 0x1000000 + the location number
	//
	// After this call, leaf nodes in the trie have the value:
	//
	// (total number of nodes in the trie) + (offset of location
	// record in the location segment)
	//
	// Absence of a record is indicated by the value 0x1000000
	// before this call, and by the value (total number of nodes
	// in the trie) after this call.

	int trie_size = std::distance(trie.nodes_begin(), trie.nodes_end());

	for(std::vector<binary_trie::node>::iterator it = trie.nodes_begin();
	    it != trie.nodes_end(); ++it)
	{
		if (it->edges[0] == 0x1000000) // No data
			it->edges[0] = trie_size;
		else if (it->edges[0] > 0x1000000) { // Ptr to location block
			int loc_id = it->edges[0] - 0x1000000;
			if (loc_id >= location_pos.size() || location_pos[loc_id] == -1)
				error(EX_DATAERR, 1, "Location %d exists in blocks but not in locations", loc_id);

			int offset = location_pos[loc_id] + trie_size;
			if (offset > 0xFFFFFF)
				error(EX_DATAERR, 1, "Overflow! Offset for location %d too large (0x%x > 0xFFFFFF)", loc_id, offset);
			it->edges[0] = offset;
		}
		// Any other value would indicate a non-leaf node

		if (it->edges[1] == 0x1000000) // No data
			it->edges[1] = trie_size;
		else if (it->edges[1] > 0x1000000) { // Ptr to location block
			int loc_id = it->edges[1] - 0x1000000;
			if (loc_id >= location_pos.size() || location_pos[loc_id] == -1)
				error(EX_DATAERR, 1, "Location %d exists in blocks but not in locations", loc_id);

			int offset = location_pos[loc_id] + trie_size;
			if (offset > 0xFFFFFF)
				error(EX_DATAERR, 1, "Overflow! Offset for location %d too large (0x%x > 0xFFFFFF)", loc_id, offset);
			it->edges[1] = offset;
		}
		// Any other value would indicate a non-leaf node
	}
}

void city_dat_writer::write_locations()
{
	*dat_stream << location_stream.rdbuf();

	if (dat_stream->bad())
	{
		error(EX_IOERR, errno, "%s", dat_file_name.c_str());
	}
}

void city_dat_writer::write_structure_info(binary_trie &trie)
{
	int trie_size = std::distance(trie.nodes_begin(), trie.nodes_end());

	const char structure_info[7] = { (char)0xFF,
					 (char)0xFF,
					 (char)0xFF,
					 (char)database_type,
					 (char)((trie_size      ) & 0xFF),
					 (char)((trie_size >> 8 ) & 0xFF),
					 (char)((trie_size >> 16) & 0xFF)};
	dat_stream->write(structure_info, 7);
}

/** Convert location info into on-disk format
 *
 *  \param info the location info read from the .csv file:
 *
 *  info[CSV_LOCATION_FIELD_COUNTRY] is the country id
 *  info[CSV_LOCATION_FIELD_REGION] is the region
 *  info[CSV_LOCATION_FIELD_CITY] is the city
 *
 *  ... and so on.
 *
 *  \param result a vector to append the on-disk converted information
 *  to.
 *
 *  \param input_line_number input file line number (for error
 *  notifications)
 **/

void city_dat_writer::serialize_location_info(std::vector<std::string> &info,
					      const char *input_file_name,
					      int input_line_number)
{
	// First, we determine the offset of this location block.
	int loc_id = ::atoi(info[0].c_str());

	if (needed_locations.find(loc_id) == needed_locations.end()) {
		// We don't need this location, so we skip serializing
		// it altogether.

		return;
	}

	if (loc_id >= location_pos.size()) {
		// We need to add to the location table (this is the
		// usual case).
		
		while(loc_id > location_pos.size()) {
			// If some numbers were skipped in the data,
			// then we need to add some empty locations to
			// the table before we find our spot.
			location_pos.push_back(-1);
		}

		// Now we have our spot, insert this location.
		location_pos.push_back(location_stream.tellp());
	} else {
		// We already have a space in the table for this location --
		// if it's not empty, then we have two locations with the same
		// ID, and we print an error.
		if (location_pos[loc_id] != -1) {
			error_at_line(EX_DATAERR, 0, input_file_name,
				      input_line_number,
				      "Duplicate location info for ID %d",
				      loc_id);
		}
		location_pos[loc_id] = location_stream.tellp();
	}

	// Country ID
	int country_id;
	if (info[1] != "AN")
		country_id = GeoIP_id_by_code(info[1].c_str());
	else
		country_id = GeoIP_id_by_code("CW");

	if (country_id == 0) {
		error(EX_DATAERR, 1, dat_file_name.c_str(), input_line_number,
		      "Unrecognized country code: %s", info[1].c_str());
	}
	location_stream.put(country_id);

	// Region
	location_stream << info[2];
	location_stream.put('\0');

	// City
	location_stream << info[3];
	location_stream.put('\0');

	// Postal code
	location_stream << info[4];
	location_stream.put('\0');

	// Latitude
	double latitude_dbl = ::atof(info[5].c_str());
	int latitude_int = (latitude_dbl + 180) * 10000;
	location_stream.put((latitude_int >>  0) & 0xFF);
	location_stream.put((latitude_int >>  8) & 0xFF);
	location_stream.put((latitude_int >> 16) & 0xFF);

	// Longitude
	double longitude_dbl = ::atof(info[6].c_str());
	int longitude_int = (longitude_dbl + 180) * 10000;
	location_stream.put((longitude_int >>  0) & 0xFF);
	location_stream.put((longitude_int >>  8) & 0xFF);
	location_stream.put((longitude_int >> 16) & 0xFF);

	// Area code and metro code
	if (info[1] == "US") {
		int metro_code = ::atoi(info[7].c_str());
		int area_code = ::atoi(info[8].c_str());
		int area_metro_combined = metro_code * 1000 + area_code;
		location_stream.put((area_metro_combined >>  0) & 0xFF);
		location_stream.put((area_metro_combined >>  8) & 0xFF);
		location_stream.put((area_metro_combined >> 16) & 0xFF);
	}
}

/*************************************************
 * Command line and options
 *
 * This section implements the command line parsing and stores the
 * options for controlling the program's behavior.
 *************************************************/

namespace {

	struct cmdline {
		const char *ip_block_csv_file_name;
		const char *location_csv_file_name;
		const char *dat_file_name;
		int address_family;
	        GeoIPDBTypes database_type;
		const char *database_info;
		bool verbose;

		cmdline(int argc, char **argv);
	};
}

cmdline::cmdline(int argc, char **argv):
	ip_block_csv_file_name("-"),
	location_csv_file_name(NULL),
	dat_file_name("-"),
	address_family(AF_INET),
	database_type(GEOIP_COUNTRY_EDITION),
	database_info(NULL),
	verbose(false)
{
	enum {
		OPT_HELP = -2
	};

	static const struct option long_options[] = {
		{ "inet", no_argument, NULL, '4' },
		{ "inet6", no_argument, NULL, '6' },
		{ "info", required_argument, NULL, 'i' },
		{ "location-csv", required_argument, NULL, 'l' },
		{ "output", required_argument, NULL, 'o' },
		{ "type", required_argument, NULL, 't' },
		{ "verbose", no_argument, NULL, 'v' },
		{ "help", no_argument, NULL, OPT_HELP },
		{ NULL, 0, NULL, 0 }
	};
	static const char *const usage = "\
Usage: %s [OPTION] [CSV-FILE]...\n\
Convert a GeoIP database from CSV to GeoIP binary format.\n\
\n\
  -4, --inet              set database type to GEOIP_COUNTRY_EDITION, v4 addresses (default)\n\
  -6, --inet6             set database type to GEOIP_COUNTRY_EDITION_V6, v6 addresses\n\
  -t, --type=TYPE         set database type explicitly (e.g. to GEOIP_CITY_EDITION_REV1)\n\
  -i, --info=TEXT         add copyright or other info TEXT to output\n\
  -l, --location-csv=FILE set location CSV file name (required for GEOIP_CITY_EDITION_REV1)\n\
  -o, --output=FILE       write the binary data to FILE, not stdout\n\
  -v, --verbose           show what is going on\n\
      --help              display this help and exit\n";

	for (;;) {
		int optret = getopt_long(argc, argv, "46i:l:o:t:v", long_options, NULL);

		if (optret == -1)
			break;
		switch (optret) {
		case '4':
			address_family = AF_INET;
			break;
		case '6':
			database_type = GEOIP_COUNTRY_EDITION_V6;
			address_family = AF_INET6;
			break;
		case 'i':
			database_info = optarg;
			if (std::strlen(database_info) > 99) {
				error(EX_USAGE, 0,
				      "Database info must not be longer than 99 bytes");
			}
			break;
		case 'l':
			location_csv_file_name = optarg;
			break;
		case 'o':
			dat_file_name = optarg;
			break;
		case 't':
			if (!strcmp(optarg, "GEOIP_COUNTRY_EDITION")) {
				database_type = GEOIP_COUNTRY_EDITION;
			} else if (!strcmp(optarg, "GEOIP_COUNTRY_EDITION_V6")) {
				database_type = GEOIP_COUNTRY_EDITION_V6;
				address_family = AF_INET6;
			} else if (!strcmp(optarg, "GEOIP_CITY_EDITION_REV1")) {
				database_type = GEOIP_CITY_EDITION_REV1;
			} else {
				error(EX_USAGE, 0,
				      "Unrecognized database type (we support GEOIP_COUNTRY_EDITION, GEOIP_COUNTRY_EDITION_V6, \
GEOIP_CITY_EDITION_REV1)");
			}
			break;
		case 'v':
			verbose = true;
			break;
		case OPT_HELP:
			std::printf(usage, program_invocation_name);
			std::exit(EX_OK);
		case '?':
			std::fprintf(stderr,
				     "Try `%s --help' for more information.\n",
				     program_invocation_name);
			std::exit(EX_USAGE);
		default:
			std::abort();
		}
	}

	if (optind < argc)
		ip_block_csv_file_name = argv[optind++];

	if (database_type == GEOIP_CITY_EDITION_REV1 && location_csv_file_name == NULL) {
		error(EX_USAGE, 0,
		      "Must specify -l option when type is GEOIP_CITY_EDITION_REV1");
	}

	if (optind < argc) {
		error(EX_USAGE, 0,
		      "Only one non-option argument is allowed");
	}
}

/*************************************************
 * Country DB reading and writing
 *
 * This section contains code implementing coverting a country .csv
 * file to a country .dat file.
 *************************************************/

namespace {

	class country_db_impl : public csv_data_reader
	{
	public:
		binary_trie trie;
		struct cmdline &cmdline;

		enum {
			CSV_FIELD_MIN_TEXT,
			CSV_FIELD_MAX_TEXT,
			CSV_FIELD_MIN_DECIMAL,
			CSV_FIELD_MAX_DECIMAL,
			CSV_FIELD_COUNTRY_CODE,
			CSV_FIELD_COUNTRY_NAME,
			CSV_FIELDS
		};

		country_db_impl(struct cmdline &cmdline);
		void convert_db(std::ostream *verbose_stream);
		void read_csv_line(const char *csv_file_name,
				   int csv_line_number,
				   std::vector<std::string> &fields);
	};

}

country_db_impl::country_db_impl(struct cmdline &in_cmdline):
	cmdline(in_cmdline),
	trie(0xFFFF00)
{ }

/** Callback for receiving .csv data (see csv_read_file()) */

void country_db_impl::read_csv_line(const char *csv_file_name,
				    int csv_line_number,
				    std::vector<std::string> &csv_fields)
{
	if (csv_fields.size() != CSV_FIELDS) {
		error_at_line(EX_DATAERR, 0, csv_file_name, csv_line_number,
			      "Wrong number of fields");
	}

	if (csv_fields[CSV_FIELD_COUNTRY_CODE] == "AN") {
		csv_fields[CSV_FIELD_COUNTRY_CODE] = "CW";
	}

	const int countryid = GeoIP_id_by_code(csv_fields[CSV_FIELD_COUNTRY_CODE].c_str());
	if (countryid == 0) {
		error_at_line(EX_DATAERR, 0, csv_file_name, csv_line_number,
			      "Unrecognized country code: %s",
			      csv_fields[CSV_FIELD_COUNTRY_CODE].c_str());
	}
	const binary_trie::edge_type leaf = 0xFFFF00 + countryid;

	union {
		struct in_addr inet;
		uint8_t inetbytes[4];
		struct in6_addr inet6;
	} minaddr, maxaddr;
	if (inet_pton(cmdline.address_family, csv_fields[CSV_FIELD_MIN_TEXT].c_str(), &minaddr) <= 0) {
		error_at_line(EX_DATAERR, 0, csv_file_name, csv_line_number,
			      "Cannot parse minimum address: %s",
			      csv_fields[CSV_FIELD_MIN_TEXT].c_str());
	}
	if (inet_pton(cmdline.address_family, csv_fields[CSV_FIELD_MAX_TEXT].c_str(), &maxaddr) <= 0) {
		error_at_line(EX_DATAERR, 0, csv_file_name, csv_line_number,
			      "Cannot parse maximum address: %s",
			      csv_fields[CSV_FIELD_MAX_TEXT].c_str());
	}
	switch (cmdline.address_family) {
	case AF_INET:
		trie.set_range(minaddr.inetbytes, maxaddr.inetbytes,
			       32, leaf);
		break;
	case AF_INET6:
		trie.set_range(minaddr.inet6.s6_addr, maxaddr.inet6.s6_addr,
			       128, leaf);
		break;
	default:
		abort();
	}
}

/** Convert a country DB from .csv to .dat. Parameters are mainly
 *  controlled by the cmdline object. verbose_stream is (if non-NULL)
 *  the stream to write verbose information to. */

void country_db_impl::convert_db(std::ostream *verbose_stream)
{
	if (verbose_stream) {
		*verbose_stream << program_invocation_name
				<< ": Reading CSV and building the trie"
				<< std::endl;
	}
	csv_read_file(*this, cmdline.ip_block_csv_file_name);

	if (verbose_stream) {
		*verbose_stream << program_invocation_name
				<< ": Optimizing" << std::endl;
	}
	trie.reorder_depth_first();
	trie.reorder_in_blocks(1024);

	if (verbose_stream) {
		*verbose_stream << program_invocation_name
				<< ": Writing output" << std::endl;
	}

	dat_writer writer(cmdline.dat_file_name, cmdline.database_type);
	writer.write_trie(trie);
	if (cmdline.database_info)
		writer.write_database_info(cmdline.database_info);
	writer.write_structure_info();
}

/*************************************************
 * City DB conversion
 *
 * This section implements converting the two .csv files storing city
 * data to a city .dat file.
 *************************************************/

namespace {

	/** Implementation for converting a city DB
	 */

	class city_db_impl : public csv_data_reader
	{
	public:
		// Trie mapping IP ranges to location blocks
		binary_trie trie;

		// Writer for .dat file
		city_dat_writer writer;

		enum {
			STAGE_READING_BLOCKS,
			STAGE_READING_LOCATIONS
		};

		// Which stage of CSV reading we're at (out of above
		// enum)
		int which_stage;

		struct cmdline &cmdline;

		enum {
			CSV_BLOCK_FIELD_MIN_DECIMAL,
			CSV_BLOCK_FIELD_MAX_DECIMAL,
			CSV_BLOCK_FIELD_LOC,
			CSV_BLOCK_FIELDS
		};

		enum {
			CSV_LOCATION_FIELD_ID,
			CSV_LOCATION_FIELD_COUNTRY,
			CSV_LOCATION_FIELD_REGION,
			CSV_LOCATION_FIELD_CITY,
			CSV_LOCATION_FIELD_POSTALCODE,
			CSV_LOCATION_FIELD_LATITUDE,
			CSV_LOCATION_FIELD_LONGITUDE,
			CSV_LOCATION_FIELD_METROCODE,
			CSV_LOCATION_FIELD_AREACODE,
			CSV_LOCATION_FIELDS
		};

		city_db_impl(struct cmdline &cmdline);
		void convert_db(std::ostream *verbose_stream);
		void read_csv_line(const char *csv_file_name,
				   int csv_line_number,
				   std::vector<std::string> &fields);

		void read_location_line(const char *csv_file_name,
					int csv_line_number,
					std::vector<std::string> &fields);
		void read_block_line(const char *csv_file_name,
				     int csv_line_number,
				     std::vector<std::string> &fields);

		// Check that a token within the "header" of the CSV
		// files is what we expect it to be, and cause a data
		// error if not.
		void check_csv_header_token(std::vector<std::string> &tokens,
					    int token_number,
					    const char *token_expected,
					    const char *csv_file_name,
					    int csv_line_number);
	};

}

city_db_impl::city_db_impl(struct cmdline &in_cmdline):
	trie(0x1000000), // We use 0x1000000 as the beginning of the
	                 // location information, since we don't know
	                 // the real value and we'll need to remap all
			 // the offsets later anyway.
	writer(in_cmdline.dat_file_name, in_cmdline.database_type),
	cmdline(in_cmdline),
	which_stage(STAGE_READING_BLOCKS)
{ }

/** Convert a city DB from .csv to .dat. Parameters are mainly
 *  controlled by the cmdline object. verbose_stream is (if non-NULL)
 *  the stream to write verbose information to. */

void
city_db_impl::convert_db(std::ostream *verbose_stream)
{
	// Read the block data from CSV
	if (verbose_stream) {
		*verbose_stream << program_invocation_name
				<< ": Reading block CSV and building the trie"
				<< std::endl;
	}

	which_stage = STAGE_READING_BLOCKS;
	csv_read_file(*this, cmdline.ip_block_csv_file_name);

	if (verbose_stream) {
		int trie_size = std::distance(trie.nodes_begin(), trie.nodes_end());

		*verbose_stream << program_invocation_name
				<< ": Done reading blocks, trie size is "
				<< trie_size
				<< std::endl;
	}

	// Read the location data from CSV
	if (verbose_stream) {
		*verbose_stream << program_invocation_name
				<< ": Reading location CSV"
				<< std::endl;
	}

	which_stage = STAGE_READING_LOCATIONS;
	csv_read_file(*this, cmdline.location_csv_file_name);

	// Optimize
	if (verbose_stream) {
		*verbose_stream << program_invocation_name
				<< ": Optimizing" << std::endl;
	}

	trie.reorder_depth_first();
	trie.reorder_in_blocks(1024);

	// Finalize offsets
	if (verbose_stream) {
		*verbose_stream << program_invocation_name
				<< ": Linking location and block data" << std::endl;
	}

	writer.finalize_location_offsets(trie);

	// Write
	if (verbose_stream) {
		*verbose_stream << program_invocation_name
				<< ": Writing output" << std::endl;
	}

	writer.write_trie(trie);
	writer.write_locations();
	if (cmdline.database_info)
		writer.write_database_info(cmdline.database_info);
	writer.write_structure_info(trie);
}

/** Callback for receiving CSV data (see csv_read_file()). We use
 *  this both for reading the location CSV and the block CSV; which
 *  stage we're at is indicated by the which_stage variable. */

void city_db_impl::read_csv_line(const char *csv_file_name,
				 int csv_line_number,
				 std::vector<std::string> &csv_fields)
{
	switch(which_stage) {
	case STAGE_READING_BLOCKS:
		read_block_line(csv_file_name, csv_line_number, csv_fields);
		break;
	case STAGE_READING_LOCATIONS:
		read_location_line(csv_file_name, csv_line_number, csv_fields);
		break;
	default:
		error(EX_SOFTWARE, 1, "Invalid which_stage value: %d", which_stage);
	}
}

/** Callback for reading one line of the block CSV. */

void city_db_impl::read_block_line(const char *csv_file_name,
				   int csv_line_number,
				   std::vector<std::string> &csv_fields)
{
	if (csv_line_number == 1)
		return; // Assume this is copyright information and
			// skip doing anything to it

	if (csv_fields.size() != CSV_BLOCK_FIELDS) {
		error_at_line(EX_DATAERR, 0, csv_file_name, csv_line_number,
			      "Wrong number of fields");
		return;
	}

	if (csv_line_number == 2) {
		// Assume this is header information -- we check it to
		// make sure we're looking at the right format of file.
		check_csv_header_token(csv_fields, CSV_BLOCK_FIELD_MIN_DECIMAL, "startIpNum",
				       csv_file_name, csv_line_number);
		check_csv_header_token(csv_fields, CSV_BLOCK_FIELD_MAX_DECIMAL, "endIpNum",
				       csv_file_name, csv_line_number);
		check_csv_header_token(csv_fields, CSV_BLOCK_FIELD_LOC, "locId",
				       csv_file_name, csv_line_number);

		// Format checks out, we're now done with this line
		return;
	}

	const int loc_id = atoi(csv_fields[CSV_BLOCK_FIELD_LOC].c_str());
	const binary_trie::edge_type leaf = 0x1000000 + loc_id;

	if (cmdline.address_family != AF_INET) {
		error(EX_SOFTWARE, 1, "IPv6 with city database is unimplemented.");
	}

	union {
		struct in_addr inet;
		uint8_t inetbytes[4];
	} minaddr, maxaddr;

	if (inet_aton(csv_fields[CSV_BLOCK_FIELD_MIN_DECIMAL].c_str(), &(minaddr.inet)) == 0) {
		error_at_line(EX_DATAERR, 1, csv_file_name, csv_line_number,
			      "Invalid min IP address");
	}
	if (inet_aton(csv_fields[CSV_BLOCK_FIELD_MAX_DECIMAL].c_str(), &(maxaddr.inet)) == 0) {
		error_at_line(EX_DATAERR, 1, csv_file_name, csv_line_number,
			      "Invalid max IP address");
	}

	writer.notify_need_location(loc_id);
	trie.set_range(minaddr.inetbytes, maxaddr.inetbytes, 32, leaf);
}

/** Callback for reading one line of the location CSV. */

void city_db_impl::read_location_line(const char *csv_file_name,
				      int csv_line_number,
				      std::vector<std::string> &csv_fields)
{
	if (csv_line_number == 1)
		return; // Assume this is copyright information and
			// skip it entirely

	if (csv_fields.size() != CSV_LOCATION_FIELDS) {
		error_at_line(EX_DATAERR, 0, csv_file_name, csv_line_number,
			      "Wrong number of fields");
		return;
	}

	if (csv_line_number == 2) {
		// Assume this is header information -- we check it to
		// make sure we're looking at the right format of file.
		check_csv_header_token(csv_fields, CSV_LOCATION_FIELD_ID, "locId",
				       csv_file_name, csv_line_number);
		check_csv_header_token(csv_fields, CSV_LOCATION_FIELD_COUNTRY, "country",
				       csv_file_name, csv_line_number);
		check_csv_header_token(csv_fields, CSV_LOCATION_FIELD_REGION, "region",
				       csv_file_name, csv_line_number);
		check_csv_header_token(csv_fields, CSV_LOCATION_FIELD_CITY, "city",
				       csv_file_name, csv_line_number);
		check_csv_header_token(csv_fields, CSV_LOCATION_FIELD_POSTALCODE, "postalCode",
				       csv_file_name, csv_line_number);
		check_csv_header_token(csv_fields, CSV_LOCATION_FIELD_LATITUDE, "latitude",
				       csv_file_name, csv_line_number);
		check_csv_header_token(csv_fields, CSV_LOCATION_FIELD_LONGITUDE, "longitude",
				       csv_file_name, csv_line_number);
		check_csv_header_token(csv_fields, CSV_LOCATION_FIELD_METROCODE, "metroCode",
				       csv_file_name, csv_line_number);
		check_csv_header_token(csv_fields, CSV_LOCATION_FIELD_AREACODE, "areaCode",
				       csv_file_name, csv_line_number);

		// Format checks out, we're now done with this line
		return;
	}

	writer.serialize_location_info(csv_fields, csv_file_name, csv_line_number);
}

void city_db_impl::check_csv_header_token(std::vector<std::string> &tokens,
					  int token_number,
					  const char *token_expected,
					  const char *csv_file_name,
					  int csv_line_number)
{
	if (tokens[token_number] != token_expected) {
		error_at_line(EX_DATAERR, 1, csv_file_name, csv_line_number,
			      "Incorrect format: field %d is \"%s\", but we expected \"%s\"",
			      token_number, tokens[token_number].c_str(), token_expected);
	}
}

/*************************************************
 * Main program
 *
 * This is the entry point.
 *************************************************/

int
main(int argc, char **argv)
{
	cmdline cmdline(argc, argv);

	std::ostream *verbose_stream;
	if (!cmdline.verbose)
		verbose_stream = NULL;
	else if (strcmp(cmdline.dat_file_name, "-") == 0)
		verbose_stream = &std::cerr;
	else
		verbose_stream = &std::cout;

	switch(cmdline.database_type) {
	case GEOIP_COUNTRY_EDITION:
	case GEOIP_COUNTRY_EDITION_V6:
		{
			country_db_impl country_db(cmdline);
			country_db.convert_db(verbose_stream);
			break;
		}

	case GEOIP_CITY_EDITION_REV1:
		{
			city_db_impl city_db(cmdline);
			city_db.convert_db(verbose_stream);
			break;
		}
	}

	if (verbose_stream) {
		*verbose_stream << program_invocation_name
				<< ": All done" << std::endl;
	}

	return 0;
}
