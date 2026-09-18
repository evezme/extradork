print("\n# --- extraDork ---\n")

keyword = input("Keyword (leave blank to skip): ").strip()
domain = input("Domain (leave blank to skip): ").strip()
file_type = input("File type (leave blank to skip): ").strip()
url_keyword = input("URL keyword (leave blank to skip): ").strip()
title_keyword = input("Title keyword (leave blank to skip): ").strip()
text_keyword = input("Text keyword (leave blank to skip): ").strip()
exact_phrase = input("Exact phrase (leave blank to skip): ").strip()
exclude_keyword = input("Exclude keyword (leave blank to skip): ").strip()
related_domain = input("Related domain (leave blank to skip): ").strip()
before_date = input("Before date (leave blank to skip): ").strip()
after_date = input("After date (leave blank to skip): ").strip()
language = input("Language (leave blank to skip): ").strip()

dork_parts = []

if keyword:
    dork_parts.append(keyword)

if domain:
    dork_parts.append(f"site:{domain}")

if file_type:
    dork_parts.append(f"filetype:{file_type}")

if url_keyword:
    dork_parts.append(f"inurl:{url_keyword}")

if title_keyword:
    dork_parts.append(f"intitle:{title_keyword}")

if text_keyword:
    dork_parts.append(f"intext:{text_keyword}")

if exact_phrase:
    dork_parts.append(f'"{exact_phrase}"')

if exclude_keyword:
    dork_parts.append(f"-{exclude_keyword}")

if related_domain:
    dork_parts.append(f"related:{related_domain}")

if before_date:
    dork_parts.append(f"before:{before_date}")

if after_date:
    dork_parts.append(f"after:{after_date}")

if language:
    dork_parts.append(f"lang:{language}")

dork = " ".join(dork_parts)

print("\n" + dork)
