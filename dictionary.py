a = {
"key":"live",
"name": "value",
"harry": "code",
"marks": "100",
"list": [1, 2, 9]
}

print(a["key"]) # Output: "value"
print(a["list"]) # Output: [1, 2, 9]
print(a.items())
# a.update ( { "friends": } )
print(a.get("name"))
a.update({"name":"kanha"})
print(a)
print(a.get("name"))