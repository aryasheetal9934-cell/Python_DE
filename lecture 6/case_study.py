visitor={"sheetal","riya","aham","nikhil","rudra","umbii","ahana","aham","riya","cheril"}
subscriber={"umbii","sheetal","ahana","nikhil","riya","ahana"}
print("my subscriber who visited my shop:", visitor & subscriber)
print("my subsciber and visitor uniqely to get total impression FOR THE day:",visitor | subscriber)
print("members who are not my subsciber but visited my shop:", visitor-subscriber)
print("members who are either subscriber or visitor but not both:",visitor^subscriber)
