from resume_parser import extract_text

text = extract_text("resume.pdf")

print(text[:1000])