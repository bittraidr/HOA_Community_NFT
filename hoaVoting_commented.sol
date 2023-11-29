// Specify the Solidity version
pragma solidity ^0.5.0;

// Importing ERC20 and ERC721 contracts from OpenZeppelin
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

// PolicyFactory contract inheriting from ERC20, ERC20Detailed, and ERC20Mintable
contract PolicyFactory is ERC20, ERC20Detailed, ERC20Mintable {
    
    // Public mapping to store the count of tokens owned by each address
    mapping(address => uint) public _currently_owned_count;
    
    // Public mapping to store the ID of each voting option
    mapping(string => uint) public optionId;

    // Public variable storing a reference to the PropertyNFT contract
    PropertyNFT public property_contract;

    // Public array storing unique options for voting
    string[] public _unique_options;
    
    // Public array storing unique owners
    address[] public _unique_owners;

    // Constructor for PolicyFactory contract
    constructor(PropertyNFT _property_contract, string memory policy_name, string memory policy_id) 
        ERC20Detailed(policy_name, policy_id, 18) public {
        
        property_contract = PropertyNFT(_property_contract);
        _unique_owners = property_contract.view_unique_owners();

        // Initialize token ownership count for each unique owner
        for (uint256 i; i < _unique_owners.length; i++) {
            _currently_owned_count[_unique_owners[i]] = property_contract.currently_owned_count(_unique_owners[i]);
        }

        // Mint tokens to owners based on their ownership count
        for (uint256 i; i < _unique_owners.length; i++) {
            _mint(_unique_owners[i], _currently_owned_count[_unique_owners[i]]);
        }
    }

    // Function to view the count of unique voting options
    function view_unique_options_count() public view returns (uint) {
        return _unique_options.length;
    }

    // Vote function allowing users to vote on a specific option
    function vote(string memory option) public {
        bool doesListContainElement = false;
        require(balanceOf(msg.sender) > 0, "Sorry, you cannot vote right now!");

        // Update the option ID based on the voter's balance
        optionId[option] += balanceOf(msg.sender);

        // Check if the option is already in the unique options list
        for (uint i = 0; i < _unique_options.length; i++) {
            if (keccak256(abi.encodePacked(option)) == keccak256(abi.encodePacked(_unique_options[i]))) {
                doesListContainElement = true;
                break;
            }
        }

        // Add the option to the unique options list if not present
        if (!doesListContainElement) {
            _unique_options.push(option);
        }

        // Burn the voter's tokens after voting
        _burn(msg.sender, balanceOf(msg.sender));
    }
}

// PropertyNFT contract inheriting from ERC721Full
contract PropertyNFT is ERC721Full {
    
    // Property structure to store property details
    struct property {
        string propertyAddress;
        string neighborhood;
    }

    // Mapping to associate property ID with property details
    mapping(uint256 => property) public hoaPortfolio;
    
    // Mapping to store the count of properties owned by each address
    mapping(address => uint) public currently_owned_count;

    // Array to store unique owners
    address[] public unique_owners;

    // Constructor for PropertyNFT contract
    constructor() public ERC721Full("Property", "PROP") {}

    // Function to view the list of unique owners
    function view_unique_owners() public view returns (address[] memory) {
        return unique_owners;
    }

    // Function to get the count of properties owned by a specific address
    function get_currently_owned_count(address owner_address) public view returns (uint) {
        return currently_owned_count[owner_address];
    }

    // Function to remove an owner from the unique owners list if they own no properties
    function remove_owner_from_list(address owner_address) public {
        if (currently_owned_count[owner_address] == 0) {
            for (uint256 i; i < unique_owners.length; i++) {
                if (unique_owners[i] == owner_address) {
                    unique_owners[i] = unique_owners[unique_owners.length - 1];
                    unique_owners.pop();
                    break;
                }
            }
        }
    }

    // Function to register a new property and mint an NFT for it
    function registerProperty(
        address propertyOwner,
        string memory propertyAddress,
        string memory neighborhood,
        string memory propURI
    ) public returns (uint256) {
        uint256 propId = totalSupply();
        if (currently_owned_count[propertyOwner] == 0) {
            unique_owners.push(propertyOwner);
        }
        _mint(propertyOwner, propId);
        _setTokenURI(propId, propURI);
        hoaPortfolio[propId] = property(propertyAddress, neighborhood);
        currently_owned_count[propertyOwner] += 1;
        return propId;
    }
}
