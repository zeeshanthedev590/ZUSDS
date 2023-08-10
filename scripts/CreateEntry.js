const fs = require("fs");
const path = require("path");

function addEntry(type, data) {
  try {
    const schemaRaw = fs.readFileSync(
      path.join(__dirname, "../db/dbdata.json")
    );
    const schema = JSON.parse(schemaRaw);

    if (!schema[type]) {
      console.log(`Invalid entry type: ${type}`);
      return;
    }

    const fields = schema[type].fields;
    const entry = {};

    for (let i = 0; i < fields.length; i++) {
      entry[fields[i]] = data[i] || null;
    }

    const filename = path.join(__dirname, `../db/${type.toLowerCase()}.json`);
    const rawData = fs.readFileSync(filename);
    const jsonData = JSON.parse(rawData);

    if (!Array.isArray(jsonData)) {
      console.log(`Invalid JSON data in ${type} file.`);
      return;
    }

    jsonData.push(entry);
    fs.writeFileSync(filename, JSON.stringify(jsonData, null, 2));
    console.log(`New ${type.toLowerCase()} entry added successfully.`);
  } catch (error) {
    console.error(`Error adding ${type.toLowerCase()} entry:`, error);
  }
}

// Example usage for adding a new user entry without specifying fields:

// const newUserInput = ["user123", "pass123"];
// addEntry("Users", newUserInput);

// Example usage for adding a new post entry without specifying fields:

// const newPostInput = ["user123", "This is a new post."];
// addEntry("Posts", newPostInput);
