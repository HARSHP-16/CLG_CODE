import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.HashMap;

public class LocationSelector extends JFrame {
    private JComboBox<String> stateCombo, districtCombo, talukaCombo;
    private HashMap<String, String[]> districtMap = new HashMap<>();
    private HashMap<String, String[]> talukaMap = new HashMap<>();

    public LocationSelector() {
        setTitle("Location Selector");
        setSize(400, 250);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null); // Center the window

        // Initialize data
        initializeData();

        // Create components
        JLabel stateLabel = new JLabel("Select State:");
        stateCombo = new JComboBox<>(districtMap.keySet().toArray(new String[0]));

        JLabel districtLabel = new JLabel("Select District:");
        districtCombo = new JComboBox<>();

        JLabel talukaLabel = new JLabel("Select Taluka:");
        talukaCombo = new JComboBox<>();

        JButton submitButton = new JButton("Submit");

        // Add listeners
        stateCombo.addActionListener(e -> updateDistricts());
        districtCombo.addActionListener(e -> updateTalukas());

        submitButton.addActionListener(e -> showSelection());

        // Layout
        setLayout(new GridLayout(4, 2, 10, 10));
        add(stateLabel);
        add(stateCombo);
        add(districtLabel);
        add(districtCombo);
        add(talukaLabel);
        add(talukaCombo);
        add(new JLabel()); // empty cell
        add(submitButton);

        // Set initial selections
        updateDistricts();
    }

    private void initializeData() {
        // State → Districts
        districtMap.put("Maharashtra", new String[]{"Pune", "Mumbai"});
        districtMap.put("Karnataka", new String[]{"Bengaluru", "Mysuru"});

        // District → Talukas
        talukaMap.put("Pune", new String[]{"Haveli", "Shirur"});
        talukaMap.put("Mumbai", new String[]{"Andheri", "Borivali"});
        talukaMap.put("Bengaluru", new String[]{"North", "South"});
        talukaMap.put("Mysuru", new String[]{"Nanjangud", "Hunsur"});
    }

    private void updateDistricts() {
        String selectedState = (String) stateCombo.getSelectedItem();
        String[] districts = districtMap.getOrDefault(selectedState, new String[0]);

        districtCombo.removeAllItems();
        for (String district : districts) {
            districtCombo.addItem(district);
        }

        updateTalukas();
    }

    private void updateTalukas() {
        String selectedDistrict = (String) districtCombo.getSelectedItem();
        String[] talukas = talukaMap.getOrDefault(selectedDistrict, new String[0]);

        talukaCombo.removeAllItems();
        for (String taluka : talukas) {
            talukaCombo.addItem(taluka);
        }
    }

    private void showSelection() {
        String state = (String) stateCombo.getSelectedItem();
        String district = (String) districtCombo.getSelectedItem();
        String taluka = (String) talukaCombo.getSelectedItem();

        String message = "You selected:\nState: " + state +
                         "\nDistrict: " + district +
                         "\nTaluka: " + taluka;

        JOptionPane.showMessageDialog(this, message, "Selection Summary", JOptionPane.INFORMATION_MESSAGE);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new LocationSelector().setVisible(true));
    }
}
